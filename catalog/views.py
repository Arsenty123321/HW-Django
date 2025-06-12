from django.views.generic import ListView, DetailView, TemplateView

from .models import Product


class HomeTemplateView(TemplateView):
    template_name = "catalog/index.html"


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
