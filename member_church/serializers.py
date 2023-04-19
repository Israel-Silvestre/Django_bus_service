from rest_framework_mongoengine.serializers import DocumentSerializer
from member_church.models import MemberChurches

class MemberChurchSerializer(DocumentSerializer):
  class Meta:
    model = MemberChurches
    fields = ('id', 'church_id', 'member_id', 'is_active', 'is_current')
