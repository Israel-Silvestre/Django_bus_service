from member.serializers import MemberSerializer
from member.models import Members
from rest_framework_mongoengine import viewsets #, permissions

class MemberViewSet(viewsets.ModelViewSet):
  queryset = Members.objects.all()
  serializer_class = MemberSerializer
  # permission_classes = [permissions.IsAuthenticated]