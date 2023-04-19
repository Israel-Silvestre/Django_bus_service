from rest_framework_mongoengine.serializers import DocumentSerializer
from member_bus.models import MemberBuses

class MemberBusSerializer(DocumentSerializer):
  class Meta:
    model = MemberBuses
    fields = ('id', 'bus_id', 'member_id')
