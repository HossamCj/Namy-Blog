from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .serializers import PropertySerializer
from .models import Property


class PropertyAPIList(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyAPIDetail(RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer