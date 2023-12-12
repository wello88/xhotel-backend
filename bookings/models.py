# bookings/models.py

from django.db import models

class HotelBooking(models.Model):
    room_id = models.AutoField(primary_key=True,unique=True)    
    guest_name = models.CharField(max_length=255)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    room_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default="Booked")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  

    def _str_(self):
        return f"{self.guest_name}'s Booking ({self.room_id})"