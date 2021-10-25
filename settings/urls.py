from django.urls import path

from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('search', home_search, name='home_search'),
    path('category/<slug:category>/', category_filter, name='category_filter'),
    path('contact-us/', contact_us, name='contact_us')
]