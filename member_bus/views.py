from member_bus.serializers import MemberBusSerializer
from member_bus.models import MemberBuses
from rest_framework import mixins
from rest_framework_mongoengine import viewsets #, permissions

class MemberBusViewSet(mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
  queryset = MemberBuses.objects.all()
  serializer_class = MemberBusSerializer
  # permission_classes = [permissions.IsAuthenticated]