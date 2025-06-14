from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Blog


class BlogListView(ListView):
    model = Blog
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    context_object_name = "blog"

    def get_object(self, queryset=None):
        blog = super().get_object(queryset)
        blog.views_count += 1
        blog.save()
        return blog


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "blog/blog_form.html"
    fields = ("title", "content", "preview")
    success_url = reverse_lazy("blog:blogs_list")


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = "blog/blog_form.html"
    fields = ("title", "content", "preview")
    success_url = reverse_lazy("blog:blogs_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    context_object_name = "blog"
    success_url = reverse_lazy("blog:blogs_list")
