from django.urls import path

from .views import *
from .api_view import *


urlpatterns = [
    path('property-list/', PropertyList.as_view(), name='property_list'),
    path('property/<slug>/', PropertyDetail.as_view(), name='property_detail'),

    # API's
    path('property/api/list/', PropertyAPIList.as_view(), name='property_api_list'),
    path('property/api/<int:pk>/', PropertyAPIDetail.as_view(), name='property_api_detail'),
]