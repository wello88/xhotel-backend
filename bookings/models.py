# bookings/models.py
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255,primary_key=True)
    description = models.TextField()
    location = models.CharField(max_length=255)
    average_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    description=models.TextField()
    room_id = models.IntegerField(primary_key=True)
    room_name=models.CharField(max_length=100)
    room_price=models.PositiveIntegerField()
    room_type = models.CharField(
        max_length=50,
        choices=[
            ('single', 'Single Room'),
            ('double', 'Double Room'),
            ('twin', 'Twin Room'),  
            ('queen', 'Queen Room'),
            ('king', 'King Room'),
            ('suite', 'Suite'),
            ('connecting', 'Connecting Room'),
            ('adjoining', 'Adjoining Room'),
            ('deluxe', 'Deluxe Room'),
            ('executive', 'Executive Room'),
            ('penthouse', 'Penthouse Suite'),
            ('studio', 'Studio Apartment'),
            ('apartment', 'One-Bedroom Apartment'),
            ('villa', 'Villa'),
            ('cottage', 'Cottage'),
            ('chalet', 'Chalet'),
            ('bungalow', 'Bungalow'),
        ]
    )
    # room_image = models.ImageField(upload_to='room_images/', null=True, blank=False)


    def __str__(self):
        return f"{self.hotel.name} - Room {self.room_id}"  






from django.db import models
from .models import Room
from accounts.models import CustomUser

class HotelBooking(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    adults = models.PositiveIntegerField()
    kids = models.PositiveIntegerField()
    
    # Add the 'total_price' field to the model
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Booking ({self.room.id})"





    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, to_field='username')  # Use username as the foreign key
