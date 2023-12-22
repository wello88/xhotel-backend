# # # bookings/models.py
# # from django.db import models
# # from django.db.models.signals import pre_save
# # from django.dispatch import receiver
# # from django.core.exceptions import ValidationError


# # class Hotel(models.Model):
# #     name = models.CharField(max_length=255)
# #     description = models.TextField()

# #     def __str__(self):
# #         return self.name

# # class Room(models.Model):
# #     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
# #     room_id = models.IntegerField(primary_key=True)
# #     room_type = models.CharField(
# #         max_length=50,
# #      choices=[
# #         ('single', 'Single Room'),
# #         ('double', 'Double Room'),
# #         ('twin', 'Twin Room'),  
# #         ('queen', 'Queen Room'),
# #         ('king', 'King Room'),#   
# #         ('suite', 'Suite'),
# #         ('connecting', 'Connecting Room'),
# #         ('adjoining', 'Adjoining Room'),
# #         ('deluxe', 'Deluxe Room'),
# #         ('executive', 'Executive Room'),
# #         ('penthouse', 'Penthouse Suite'),
# #         ('studio', 'Studio Apartment'),
# #         ('apartment', 'One-Bedroom Apartment'),
# #         ('villa', 'Villa'),
# #         ('cottage', 'Cottage'),
# #         ('chalet', 'Chalet'),
# #         ('bungalow', 'Bungalow'),
# #      ]
# #     )

# #     status = models.CharField(
# #         max_length=50,
# #         choices=[
# #             ('booked', 'Booked'),
# #             ('notbooked', 'Not Booked'),
# #         ],
# #         default='notbooked'
# #     )
# #     price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

# #     def __str__(self):
# #         return f"{self.hotel.name} - Room {self.room_id}"
    
# # class HotelBooking(models.Model):
# #     room_id = models.ForeignKey(Room, on_delete=models.CASCADE,null=True)
# #     check_in_date = models.DateField()
# #     check_out_date = models.DateField()

# #     def __str__(self):
# #         return f"Booking {self.id}"

# # @receiver(pre_save, sender=HotelBooking)
# # def check_booking_dates(sender, instance, **kwargs):
# #     conflicting_bookings = HotelBooking.objects.filter(
# #         room=instance.room,
# #         check_in_date__lt=instance.check_out_date,
# #         check_out_date__gt=instance.check_in_date,
# #     )

# #     if conflicting_bookings.exists():
# #         raise ValidationError("This room is already booked for the specified dates.")
    














# from accounts.models import CustomUser  # Import the User model



# from django.conf import settings  # Import the settings module




# bookings/models.py
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    average_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def _str_(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
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
    
    
    
    
    
    
    
    # Access the hotel's name

# class HotelBooking(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     name=models.CharField(max_length=100,null=True)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     check_in_date = models.DateField()
#     check_out_date = models.DateField()
#     adults = models.PositiveIntegerField()
#     kids = models.PositiveIntegerField()
#     def _str_(self):
#         return f"Booking ({self.room.id})"
    
#     # def __str__(self):
#     #     return f"Booking ({self.room.room_id})"



































from accounts.models import CustomUser
from django.db import models

class HotelBooking(models.Model):
    name = models.CharField(max_length=100, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    adults = models.PositiveIntegerField()
    kids = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking ({self.room.id})"







    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, to_field='username')  # Use username as the foreign key
