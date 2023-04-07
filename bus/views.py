from bus.serializers import BusSerializer
from bus.models import Buses
from rest_framework_mongoengine import viewsets #, permissions

class BusViewSet(viewsets.ModelViewSet):
  queryset = Buses.objects.all()
  serializer_class = BusSerializer
  # permission_classes = [permissions.IsAuthenticated]