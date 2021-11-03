from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import PropertySerializer
from .models import Property


class PropertyAPIList(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyAPIDetail(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer