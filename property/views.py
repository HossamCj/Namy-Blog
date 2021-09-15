from django.shortcuts import render, get_object_or_404
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = Property.objects.filter(category=self.get_object().category)[:2]

