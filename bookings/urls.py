# bookings/urls.py
from django.urls import path
from .views import HotelBookingListCreateView
from django.urls import include

urlpatterns = [
     path('create/', HotelBookingListCreateView.as_view(), name='create_booking'),
   
]