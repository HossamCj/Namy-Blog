from django.urls import path

from .views import *
from .api_view import *


urlpatterns = [
    path('blog/posts/', PostList.as_view(), name='post_list'),
    path('blog/posts/<str:slug>/', PostDetail.as_view(), name='post_detail'),

    path('blog/categories/<slug>/', PostsByCategory.as_view(), name='post_by_category'),
    path('blog/tags/<slug>/', PostsByTags.as_view(), name='post_by_tag'),

    # API
    path('blog/api/api-list/', post_list_api, name='post_list_api'),
    path('blog/api/<int:pk>/', post_detail_api, name='post_detail_api'),
]