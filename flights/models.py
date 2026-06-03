from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


# Model 1: Destination
class Destination(models.Model):
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.CharField(max_length=200, blank=True, null=True)  # For simple image linking

    def __str__(self):
        return f"{self.city}, {self.country}"


# Model 2: Flight (Linked to Destination)
class Flight(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    flight_number = models.CharField(max_length=10, unique=True)
    departure_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField(default=150)

    def __str__(self):
        return f"{self.flight_number} to {self.destination.city}"


# Model 3: Reservation (Linked to User and Flight)
class Reservation(models.Model):
    SEAT_CLASSES = [
        ('economy', 'Economy Class'),
        ('business', 'Business Class'),
        ('first', 'First Class'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=20)
    seat_class = models.CharField(max_length=10, choices=SEAT_CLASSES)
    extra_luggage = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Server-side validation logic
        if self.flight.departure_time < timezone.now():
            raise ValidationError("Cannot book a flight that has already departed.")