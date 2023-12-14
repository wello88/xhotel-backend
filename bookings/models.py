# # bookings/models.py
# from django.db import models
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from django.core.exceptions import ValidationError


# class Hotel(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()

#     def __str__(self):
#         return self.name

# class Room(models.Model):
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     room_id = models.IntegerField(primary_key=True)
#     room_type = models.CharField(
#         max_length=50,
#      choices=[
#         ('single', 'Single Room'),
#         ('double', 'Double Room'),
#         ('twin', 'Twin Room'),  
#         ('queen', 'Queen Room'),
#         ('king', 'King Room'),#   
#         ('suite', 'Suite'),
#         ('connecting', 'Connecting Room'),
#         ('adjoining', 'Adjoining Room'),
#         ('deluxe', 'Deluxe Room'),
#         ('executive', 'Executive Room'),
#         ('penthouse', 'Penthouse Suite'),
#         ('studio', 'Studio Apartment'),
#         ('apartment', 'One-Bedroom Apartment'),
#         ('villa', 'Villa'),
#         ('cottage', 'Cottage'),
#         ('chalet', 'Chalet'),
#         ('bungalow', 'Bungalow'),
#      ]
#     )

#     status = models.CharField(
#         max_length=50,
#         choices=[
#             ('booked', 'Booked'),
#             ('notbooked', 'Not Booked'),
#         ],
#         default='notbooked'
#     )
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     def __str__(self):
#         return f"{self.hotel.name} - Room {self.room_id}"
    
# class HotelBooking(models.Model):
#     room_id = models.ForeignKey(Room, on_delete=models.CASCADE,null=True)
#     check_in_date = models.DateField()
#     check_out_date = models.DateField()

#     def __str__(self):
#         return f"Booking {self.id}"

# @receiver(pre_save, sender=HotelBooking)
# def check_booking_dates(sender, instance, **kwargs):
#     conflicting_bookings = HotelBooking.objects.filter(
#         room=instance.room,
#         check_in_date__lt=instance.check_out_date,
#         check_out_date__gt=instance.check_in_date,
#     )

#     if conflicting_bookings.exists():
#         raise ValidationError("This room is already booked for the specified dates.")
    

































































# #     room_type = models.CharField(
# #         max_length=50,
# #         choices=ROOM_TYPE_CHOICES,
# #     )

# #     STATUS_CHOICES = [
# #         ('booked', 'Booked'),
# #         ('notbooked', 'Not Booked'),
# #     ]
    
# #     status = models.CharField(
# #         max_length=50,
# #         choices=STATUS_CHOICES,
# #         default='booked'  # You can set the default status as 'booked' if you want.
# #     )   
# #     price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  

# #     def __str__(self):
# #         return f"{self.hotel.name} - Room {self.room_id}"


# #     def get_available_dates(self):
# #         booked_dates = HotelBooking.objects.filter(
# #             room=self,
# #             check_in_date__lt=models.F('check_out_date'),
# #             check_out_date__gt=models.F('check_in_date'),
# #         ).values_list('check_in_date', 'check_out_date')

# #         booked_date_ranges = [(check_in, check_out) for check_in, check_out in booked_dates]

# #         if not booked_date_ranges:
# #             return [{'earliest': None, 'latest': None}]

# #         earliest_check_in = min(check_in for check_in, _ in booked_date_ranges)
# #         latest_check_out = max(check_out for _, check_out in booked_date_ranges)

# #         return [{'earliest': earliest_check_in, 'latest': latest_check_out}]






# # class Room(models.Model):
# #     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
# #     room_id = models.IntegerField(primary_key=True)
# #     room_type = models.CharField(max_length=50, choices=[(room, room) for room in [
# #         'Single Room', 'Double Room', 'Twin Room', 'Queen Room', 'King Room',
# #         'Suite', 'Connecting Room', 'Adjoining Room', 'Deluxe Room',
# #         'Executive Room', 'Penthouse Suite', 'Studio Apartment',
# #         'One-Bedroom Apartment', 'Villa', 'Cottage', 'Chalet', 'Bungalow',
# #     ]])
# #     status = models.CharField(max_length=50, choices=[('booked', 'Booked'), ('notbooked', 'Not Booked')], default='booked')
# #     price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

# #     def __str__(self):
# #         return f"{self.hotel.name} - Room {self.room_id}"

# #     def get_available_dates(self):
# #         booked_dates = HotelBooking.objects.filter(
# #             room=self,
# #             check_in_date__lt=models.F('check_out_date'),
# #             check_out_date__gt=models.F('check_in_date'),
# #         ).values_list('check_in_date', 'check_out_date')

# #         booked_date_ranges = [(check_in, check_out) for check_in, check_out in booked_dates]

# #         if not booked_date_ranges:
# #             return [{'earliest': None, 'latest': None}]

# #         earliest_check_in = min(check_in for check_in, _ in booked_date_ranges)
# #         latest_check_out = max(check_out for _, check_out in booked_date_ranges)

# #         return [{'earliest': earliest_check_in, 'latest': latest_check_out}]



# # class HotelBooking(models.Model):
# #     id = models.AutoField(primary_key=True)  # Change to AutoField for automatic ID assignment
# #     room = models.ForeignKey(Room, on_delete=models.CASCADE)
# #     check_in_date = models.DateField()
# #     check_out_date = models.DateField()

# #     def __str__(self):
# #         return f"Booking {self.id}"

    
# # @receiver(pre_save, sender=HotelBooking)
# # def check_booking_dates(sender, instance, **kwargs):
# #     conflicting_bookings = HotelBooking.objects.filter(
# #         room=instance.room_id,
# #         check_in_date__lt=instance.check_out_date,
# #         check_out_date__gt=instance.check_in_date,
# #     )

# #     if conflicting_bookings.exists():
# #         raise ValidationError("This room is already booked for the specified dates.")

    

















# bookings/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_id = models.IntegerField(primary_key=True)
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

    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('notbooked', 'Not Booked'),
    ]
    
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='booked'
    )

    def __str__(self):
        return f"{self.hotel} - Room {self.room_id}"
















# bookings/models.py

class HotelBooking(models.Model):
    # room = models.ForeignKey(Room, on_delete=models.CASCADE)
    roomid=models.IntegerField(primary_key=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"Booking ({self.roomid})"
