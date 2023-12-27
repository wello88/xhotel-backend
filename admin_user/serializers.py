#room for admin user
from rest_framework import serializers
from bookings.models import Room,Hotel
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from bookings.models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class HotelUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    hotel = serializers.CharField(source='hotel.name')  # استخدام source لتحديد أننا نريد استخدام اسم الفندق

    class Meta:
        model = Room
        fields = '__all__'

    def create(self, validated_data):
        hotel_name = validated_data.pop('hotel')['name']
        
        # قم بالبحث عن الفندق بناءً على اسمه
        existing_hotel = Hotel.objects.filter(name=hotel_name).first()

        # إذا وجد الفندق، استخدمه. إلا فقم برفع خطأ
        if existing_hotel:
            hotel = existing_hotel
        else:
            raise ValidationError({'hotel': f'Hotel with name "{hotel_name}" does not exist.'})

        room = Room.objects.create(hotel=hotel, **validated_data)
        return room






# serializers.py
from rest_framework import serializers
from .models import Programs

class ProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programs
        fields = '__all__'

# serializers.py
from rest_framework import serializers

class ProgramsUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programs
        fields = '__all__'



# serializers.py
from rest_framework import serializers
from bookings.models import Room

class RoomUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['description', 'room_name', 'room_price', 'room_type']

    # You can add any extra validation or custom logic here if needed
