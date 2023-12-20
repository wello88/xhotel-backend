# profile/serializers.py
from rest_framework import serializers
from accounts.models import CustomUser  # Import CustomUser model from accounts app

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']  # Add other fields as needed
