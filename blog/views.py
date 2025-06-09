from django.views.generic import ListView, DetailView

from .models import Blog


class BlogListView(ListView):
    model = Blog
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = "blog"

    def get_object(self, queryset=None):
        blog = super().get_object(queryset)
        blog.views_count += 1
        blog.save()
        return blog
