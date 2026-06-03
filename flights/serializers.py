from rest_framework import serializers
from .models import Flight, Destination

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    destination = DestinationSerializer()
    class Meta:
        model = Flight
        fields = ['id', 'flight_number', 'destination', 'departure_time', 'price']