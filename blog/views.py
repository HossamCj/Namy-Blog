from django.db.models import Count
from django.db.models.query_utils import Q
from django.views.generic import ListView, DetailView
from taggit.models import Tag

from .models import *


class PostList(ListView):
    model = Post
    paginate_by = 4

    def get_queryset(self):
        search = self.request.GET.get('s', '')
        object_list = Post.objects.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )
        return object_list


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().annotate(post_count=Count('post_category'))
        context['tags'] = Tag.objects.all()
        context['recent_posts'] = Post.objects.all()[:3]
        return context


class PostsByCategory(ListView):
    model = Post

    def get_queryset(self):
        slug = self.kwargs['slug']
        object_list = Post.objects.filter(
            Q(category__name__icontains=slug)
        )
        return object_list


class PostsByTags(ListView):
    model = Post

    def get_queryset(self):
        slug = self.kwargs['slug']
        object_list = Post.objects.filter(
            Q(tags__name__icontains=slug)
        )
        return object_list













