# payments/models.py
from django.db import models
from django.utils import timezone
from bookings.models import HotelBooking

class Payment(models.Model):
    room_booking = models.ForeignKey(HotelBooking, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment for Room {self.room_booking.room.room_id} on {self.payment_date}"

    @classmethod
    def create_payment(cls, room_booking, payment_amount, payment_method):
        payment_date = timezone.now()
        
        payment = cls.objects.create(
            room_booking=room_booking,
            payment_amount=payment_amount,
            payment_date=payment_date,
            payment_method=payment_method
        )
        return payment
