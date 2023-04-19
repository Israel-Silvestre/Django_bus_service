from member_church.serializers import MemberChurchSerializer
from member_church.models import MemberChurches
from rest_framework import mixins
from rest_framework_mongoengine import viewsets #, permissions

class MemberChurchViewSet(mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
  queryset = MemberChurches.objects.all()
  serializer_class = MemberChurchSerializer
  # permission_classes = [permissions.IsAuthenticated]