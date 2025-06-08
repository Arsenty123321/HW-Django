from django.views.generic import ListView

from .models import Blog


class BlogListView(ListView):
    model = Blog
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)
