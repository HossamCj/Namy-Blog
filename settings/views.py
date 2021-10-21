from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'settings/home.html', context)