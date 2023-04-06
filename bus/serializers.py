from rest_framework import serializers
from bus.models import Bus
class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = [
            'id',
            'description',
            'number_of_seats',
            'departure_date',
            'return_date'
        ]