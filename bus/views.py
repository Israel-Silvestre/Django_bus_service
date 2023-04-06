from bus.serializers import BusSerializer
from rest_framework import viewsets, permissions
from bus.models import Bus

class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    # permission_classes = [permissions.IsAuthenticated]