from django.urls import path
import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flights/', views.flight_list, name='flight_list'),
    path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('my-reservations/', views.my_reservations, name='my_reservations'),
    path('edit-reservation/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),

    # API
    path('api/flights/', views.api_flight_list),
    path('api/flights/<int:pk>/', views.api_flight_detail),
]