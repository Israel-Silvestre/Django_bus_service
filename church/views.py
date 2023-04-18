from church.models import *
from church.serializers import ChurchSerializer
from rest_framework_mongoengine import generics

class ChurchList(generics.ListAPIView):
  queryset = Churches.objects.all()
  serializer_class = ChurchSerializer
