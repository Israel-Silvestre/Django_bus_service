from rest_framework_mongoengine.serializers import DocumentSerializer
from church.models import Churches

class ChurchSerializer(DocumentSerializer):
  class Meta:
    model = Churches
    fields = ('id', 'name', 'city', 'pastor')