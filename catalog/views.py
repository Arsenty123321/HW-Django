from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from .forms import ProductForm, ProductModeratorForm
from .models import Product, Category
from .services import get_products_from_cache, get_categories_from_cache, get_products_from_category


class HomeTemplateView(TemplateView):
    template_name = "catalog/index.html"


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get("id")
        context['current_category_id'] = category_id
        context['products'] = get_products_from_category(category_id)
        return context


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        queryset = get_products_from_cache()
        return queryset.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # categories = get_categories_from_cache()
        context['categories'] = get_categories_from_cache()
        return context


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        user = self.request.user

        if user.has_perm('catalog.can_unpublish_product') and not user.has_perm('is_superuser'):
            return HttpResponseForbidden("У модераторов нет прав для создания продукта.")

        form.instance.owner = user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    context_object_name = "product"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        user = self.request.user
        if user == self.object.owner or user.has_perm('catalog.can_unpublish_product'):
            return super().form_valid(form)
        return HttpResponseForbidden("У вас нет прав для удаления продукта.")
