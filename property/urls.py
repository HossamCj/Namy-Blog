from django.urls import path

from .views import *


urlpatterns = [
    path('', PropertyList.as_view(), name='property_list'),
    path('<slug>/', PropertyDetail.as_view(), name='property_detail'),
]