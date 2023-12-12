# bookings/urls.py
from django.urls import path
from .views import HotelBookingListCreateView

urlpatterns = [
     path('create/', HotelBookingListCreateView.as_view(), name='create_booking'),
   
]