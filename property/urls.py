from django.urls import path

from .views import *


urlpatterns = [
    path('property-list/', PropertyList.as_view(), name='property_list'),
    path('property/<slug>/', PropertyDetail.as_view(), name='property_detail'),
]