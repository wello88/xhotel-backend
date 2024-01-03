# serializers.py
from rest_framework import serializers
from .models import HotelBooking

from rest_framework import serializers
from .models import HotelBooking
class HotelBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelBooking
        fields = '__all__'







    def validate(self, data):
        """
        Validate the data before creating a new HotelBooking instance.
        """
        check_in_date = data.get('check_in_date')
        check_out_date = data.get('check_out_date')
        adults = data.get('adults', 0)
        kids = data.get('kids', 0)

        if check_in_date and check_out_date:
            # Calculate the number of days
            number_of_days = (check_out_date - check_in_date).days

            # Calculate the total price using the provided formula
            total_price = data['room'].room_price * number_of_days * (1 + 0.2 * adults + 0.1 * kids)

            # Add the calculated total price to the data
            data['total_price'] = total_price

        return data







        # serializers.py
from rest_framework import serializers
from .models import Room

class RoomSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_id', 'room_name', 'room_price', 'room_type']