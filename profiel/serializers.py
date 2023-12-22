# # profiel/serializers.py

# from rest_framework import serializers
# from accounts.models import CustomUser
# from bookings.models import HotelBooking

# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = [ 'username', 'email']  # Add other fields as needed

# class HotelBookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HotelBooking
#         fields = '_all_'  # Include all fields from the HotelBooking model



# profiel/serializers.py

from rest_framework import serializers
from accounts.models import CustomUser
from bookings.models import HotelBooking

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']  # Add other fields as needed

class HotelBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelBooking
        fields = '_all_'  