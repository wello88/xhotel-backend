# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    hobbies = models.CharField(max_length=255)
    password = models.CharField(max_length=128) 

    def __str__(self):
        return self.username
    


    # models.py for admin panel

from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return f"{self.hotel.name} - Room {self.room_number}"
