# bookings/urls.py
from django.urls import path
from .views import HotelBookingListCreateView

urlpatterns = [
     path('booking/', HotelBookingListCreateView.as_view(), name='booking'),
   
]