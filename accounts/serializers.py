# # accounts/serializers.py

# from rest_framework import serializers
# from .models import CustomUser

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'username', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = CustomUser(
#             username=validated_data['username'],
#             email=validated_data['email'],
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user


#     # accounts/serializers.py/changepass

# from rest_framework import serializers

# class ChangePasswordSerializer(serializers.Serializer):
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)

# class ResetPasswordEmailSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)



































# accounts/serializers.py

from rest_framework import serializers
from .models import CustomUser
from rest_framework import serializers
from .models import CustomUser
from allauth.account.signals import email_confirmed
from django.dispatch import receiver


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'username', 'first_name', 'last_name', 'country', 'zip', 'hobbies', 'password']
#         extra_kwargs = {
#             'username': {'required': True},
#             'email': {'required': True},
#             'password': {'write_only': True, 'required': True},
#             'first_name': {'required': False},
#             'last_name': {'required': False},
#             'country': {'required': False},
#             'zip': {'required': False},
#             'hobbies': {'required': False},
#         }

# from django.db import transaction


# class UserSerializer(serializers.ModelSerializer):
#     confirmation_key = serializers.CharField(write_only=True, required=False)

#     class Meta:
#         model = CustomUser
#         fields = ['email', 'username', 'first_name', 'last_name', 'country', 'zip', 'hobbies', 'password', 'confirmation_key']
#         extra_kwargs = {
#             'username': {'required': True},
#             'email': {'required': True},
#             'password': {'write_only': True, 'required': True},
#             'first_name': {'required': False},
#             'last_name': {'required': False},
#             'country': {'required': False},
#             'zip': {'required': False},
#             'hobbies': {'required': False},
#         }

#     def create(self, validated_data):
#         confirmation_key = validated_data.pop('confirmation_key', None)

#         # Wrap the creation of user and email in a transaction

#         user = CustomUser(**validated_data)
#         user.set_password(validated_data['password'])

#         if confirmation_key:
#             # If confirmation key is provided, save the user and send confirmation email
#             with transaction.atomic():
#                 user.save()
#                 email_address = user.emailaddress_set.get(email=user.email)
#                 email_address.verified = True
#                 email_address.save()

#         return user















# serializers.py

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'country', 'zip', 'hobbies']
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




















    
    # accounts/serializers.py/changepass

from rest_framework import serializers

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)