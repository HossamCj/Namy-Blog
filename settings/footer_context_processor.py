from .models import Settings


def mainfooter(request):
    footer = Settings.objects.last()
    context = {'footer': footer}
    return context