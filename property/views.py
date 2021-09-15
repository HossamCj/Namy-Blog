from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Property


class PropertyList(ListView):
    model = Property
    paginate_by = 1
    # filter
    # pagination


class PropertyDetail(DetailView):
    model = Property
    # book

