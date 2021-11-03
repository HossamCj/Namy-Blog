from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PostSerializers
from .models import Post


@api_view(['GET'])
def post_list_api(request):
    all_posts = Post.objects.all()
    data = PostSerializers(all_posts, many=True, context={'request': request}).data
    return Response({'data': data})


@api_view(['GET'])
def post_detail_api(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = PostSerializers(post, context={'request': request}).data
    return Response({'data': data})


@api_view(['GET'])
def post_filter_api(request, query):
    posts = Post.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
    )
    data = PostSerializers(posts, many=True).data
    return Response({'data': data})
