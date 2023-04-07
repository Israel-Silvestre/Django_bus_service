from rest_framework_mongoengine.serializers import DocumentSerializer
from bus.models import Buses

class BusSerializer(DocumentSerializer):
  class Meta:
    model = Buses
    fields = ('id', 'description', 'number_of_seats', 'value', 'departure_date', 'return_date')