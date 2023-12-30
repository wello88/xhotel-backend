# bookings/urls.py
from django.urls import path
from .views import HotelBookingListCreateView
from . import views
from .views import RoomBookingView
from .views import get_all_rooms,RoomSearchView,get_hotel_details,get_user_booking_info

urlpatterns = [
     path('booking/', HotelBookingListCreateView.as_view(), name='booking'),
     path('hotel-details/', get_hotel_details, name='hotel-details'),
     path('profilebooking/', get_user_booking_info, name='bookin-details'),
     path('all-rooms/', get_all_rooms, name='all-rooms'),
     path('DashBoard/', RoomBookingView.as_view(), name='room-count'), 
     path('room-search/', RoomSearchView.as_view(), name='room-search'),
]
