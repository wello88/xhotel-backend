# accounts/serializers.py

from rest_framework import serializers
from .models import CustomUser
from rest_framework import serializers
from .models import CustomUser
from allauth.account.signals import email_confirmed
from django.dispatch import receiver


# serializers.py

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password', 'first_name', 'last_name', 'country', 'zip', 'hobbies']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True},
            'first_name': {'required': False},
            'last_name': {'required': False},
            'country': {'required': False},
            'zip': {'required': False},
            'hobbies': {'required': False},
        }
         
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
















# #room for admin user
# from rest_framework import serializers
# from bookings.models import Room,Hotel
# from rest_framework.exceptions import ValidationError

# # serializers.py
# # serializers.py
# from rest_framework import serializers
# from bookings.models import Hotel

# class HotelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Hotel
#         fields = '__all__'

# class RoomSerializer(serializers.ModelSerializer):
#     hotel = serializers.CharField(source='hotel.name')  # استخدام source لتحديد أننا نريد استخدام اسم الفندق

#     class Meta:
#         model = Room
#         fields = '__all__'

#     def create(self, validated_data):
#         hotel_name = validated_data.pop('hotel')['name']
        
#         # قم بالبحث عن الفندق بناءً على اسمه
#         existing_hotel = Hotel.objects.filter(name=hotel_name).first()

#         # إذا وجد الفندق، استخدمه. إلا فقم برفع خطأ
#         if existing_hotel:
#             hotel = existing_hotel
#         else:
#             raise ValidationError({'hotel': f'Hotel with name "{hotel_name}" does not exist.'})

#         room = Room.objects.create(hotel=hotel, **validated_data)
#         return room









    
    # accounts/serializers.py/changepass

from rest_framework import serializers

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)