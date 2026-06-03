from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Flight, Reservation, Destination
from .forms import ReservationForm
from .serializers import FlightSerializer


# View 1: Home
def home(request):
    destinations = Destination.objects.all()[:3]
    return render(request, 'flights/home.html', {'destinations': destinations})


# View 2: Flight List
def flight_list(request):
    flights = Flight.objects.all().order_by('departure_time')
    return render(request, 'flights/flight_list.html', {'flights': flights})


# View 3: Create Reservation (Protected)
@login_required
def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.flight = flight
            reservation.save()
            messages.success(request, "Flight booked successfully!")
            return redirect('my_reservations')
    else:
        form = ReservationForm()

    return render(request, 'flights/booking_form.html', {'form': form, 'flight': flight})


# View 4: User Reservations
@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'flights/my_reservations.html', {'reservations': reservations})


# Edit Reservation View
@login_required
def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id, user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Reservation updated.")
            return redirect('my_reservations')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'flights/booking_form.html', {'form': form, 'flight': reservation.flight, 'is_edit': True})


# REST API Endpoints
@api_view(['GET'])
def api_flight_list(request):
    flights = Flight.objects.all()
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_flight_detail(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    serializer = FlightSerializer(flight)
    return Response(serializer.data)