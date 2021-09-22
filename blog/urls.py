from django.urls import path

from .views import *


urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<str:slug>/', PostDetail.as_view(), name='post_detail'),

    path('categories/<slug>/', PostsByCategory.as_view(), name='post_by_category'),
    path('tags/<slug>/', PostsByTags.as_view(), name='post_by_tag'),
]