# bookings/serializers.py

# from rest_framework import serializers
# from .models import HotelBooking,Room
# class HotelBookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HotelBooking
#         fields = '__all__'



# from .models import Room

# class RoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Room
#         fields = ['room_id', 'hotel', 'room_type', 'status', 'price']

# bookings/serializers.py

# from rest_framework import serializers
# from .models import HotelBooking, Room

# class RoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Room
#         fields = ['room_id', 'hotel', 'room_type', 'status', 'price']

# class HotelBookingSerializer(serializers.ModelSerializer):
#     room_data = RoomSerializer(read_only=True)  # Add this line to include room data during GET requests

#     class Meta:
#         model = HotelBooking
#         fields = ['id', 'check_in_date', 'check_out_date', 'room_id', 'room_data']

#     def create(self, validated_data):
#         # Extract room_id from the validated data
#         room_id = validated_data.pop('room_id')

#         # Get the Room object based on room_id
#         room = Room.objects.get(room_id=room_id)

#         # Create the HotelBooking instance with the Room object
#         booking = HotelBooking.objects.create(room=room, **validated_data)
#         return booking
# # bookings/serializers.py

# from rest_framework import serializers
# from .models import HotelBooking, Room

# class RoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Room
#         fields = ['room_id', 'room_type', 'status', 'price']
# # bookings/serializers.py
# class HotelBookingSerializer(serializers.ModelSerializer):
#     room_data = RoomSerializer(read_only=True)

#     class Meta:
#         model = HotelBooking
#         fields = ['check_in_date', 'check_out_date', 'room_data']

#     def validate(self, data):
#         room = data['room_data']
#         check_in_date = data['check_in_date']
#         check_out_date = data['check_out_date']

#         conflicting_bookings = HotelBooking.objects.filter(
#             room=room,
#             check_in_date__lt=check_out_date,
#             check_out_date__gt=check_in_date,
#         )

#         if conflicting_bookings.exists():
#             raise serializers.ValidationError("This room is already booked for the specified dates.")

#         if check_in_date < room['available_dates']['earliest'] or check_out_date > room['available_dates']['latest']:
#             raise serializers.ValidationError("Invalid dates. Check room availability.")

#         return data



# # bookings/serializers.py

# from rest_framework import serializers
# from .models import HotelBooking, Room
# from rest_framework import serializers
# from .models import HotelBooking, Room

# class RoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Room
#         fields = ['room_id', 'hotel', 'room_type', 'status', 'price']

# class HotelBookingSerializer(serializers.ModelSerializer):
#     room_data = RoomSerializer(read_only=True)

#     class Meta:
#         model = HotelBooking
#         fields = ['check_in_date', 'check_out_date', 'room_data',]

#     def validate(self, data):
#         room_id = data['room_data']['room_id']
#         check_in_date = data['check_in_date']
#         check_out_date = data['check_out_date']

#         try:
#             room = Room.objects.get(room_id=room_id)
#         except Room.DoesNotExist:
#             raise serializers.ValidationError("Room not found.")

#         data['room_data'] = room

#         conflicting_bookings = HotelBooking.objects.filter(
#             room=room,
#             check_in_date__lt=check_out_date,
#             check_out_date__gt=check_in_date,
#         )

#         if conflicting_bookings.exists():
#             raise serializers.ValidationError("This room is already booked for the specified dates.")

#         if check_in_date < room['available_dates']['earliest'] or check_out_date > room['available_dates']['latest']:
#             raise serializers.ValidationError("Invalid dates. Check room availability.")

#         return data
















# serializers.py
from rest_framework import serializers
from .models import HotelBooking

from rest_framework import serializers
from .models import HotelBooking
class HotelBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelBooking
        fields = '__all__'














        # serializers.py
from rest_framework import serializers
from .models import Room

class RoomSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_id', 'room_name', 'room_price', 'room_type']