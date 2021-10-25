from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render
from django.db.models.query_utils import Q

from property.models import *

from blog.models import Post


def home(request):
    places = Place.objects.all().annotate(property_count=Count('property_place'))
    categories = Category.objects.all()
    restaurants_list = Property.objects.filter(category__name='Restaurants')[:5]
    hotels_list = Property.objects.filter(category__name='Hotels')[:4]
    places_list = Property.objects.filter(category__name='Places')[:4]

    recent_posts = Post.objects.all()[:4]

    users_count = User.objects.all().count()
    places_count = Property.objects.filter(category__name='Places').count()
    hotels_count = Property.objects.filter(category__name='Hotels').count()
    restaurants_count = Property.objects.filter(category__name='Restaurants').count()

    context = {
        'places': places,
        'categories': categories,
        'restaurants_list': restaurants_list,
        'hotels_list': hotels_list,
        'places_list': places_list,
        'recent_posts': recent_posts,
        'users_count': users_count,
        'places_count': places_count,
        'hotels_count': hotels_count,
        'restaurants_count': restaurants_count,
    }
    return render(request, 'settings/home.html', context)


def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')

    property_list = Property.objects.filter(
        Q(name__icontains=name) &
        Q(place__name__icontains=place)
    )
    context = {
        'property_list': property_list,
    }

    return render(request, 'settings/home_search.html', context)


def category_filter(request, category):
    category = Category.objects.get(name=category)
    property_list = Property.objects.filter(category=category)
    context = {
        'property_list': property_list,
    }

    return render(request, 'settings/home_search.html', context)