# bookings/urls.py
from django.urls import path
from .views import HotelBookingListCreateView
from . import views
# ,count_users_booked_hotel
from .views import get_all_rooms
from .views import get_hotel_details

urlpatterns = [
     path('booking/', HotelBookingListCreateView.as_view(), name='booking'),
     path('count-users-booked/',views.count_users_booked_hotel, name='count_users_booked_hotel'),
     path('count-hotels/', views.count_hotels, name='count_hotels'),
     path('count-rooms/', views.count_rooms, name='count_rooms'),
     path('all-rooms/', get_all_rooms, name='all-rooms'),
     path('hotel-details/', get_hotel_details, name='hotel-details'),
     #  path('calculate_price/<int:booking_id>/', create_price, name='create_price'),

     
]
# # booking/urls.py

# from django.urls import path
# from .views import CalculatePriceView

# urlpatterns = [
#     path('calculate_price/<int:booking_id>/', CalculatePriceView.as_view(), name='calculate_price'),
#     # Add other URL patterns as needed
# ]
