from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *


app_name = 'accounts'


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('profile/my-reservation/', myreservation, name='my_reservation'),
    path('profile/my-listing/', mylisting, name='my_listing'),

    path('profile/edit/', profile_edit, name='profile_edit'),
]


