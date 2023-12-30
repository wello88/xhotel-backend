# views.py
from django.shortcuts import render, redirect
from .models import Payment
from bookings.models import HotelBooking
from django.utils import timezone

def make_payment(request, booking_id):
    try:
        # Get the HotelBooking instance for the given booking_id
        booking = HotelBooking.objects.get(id=booking_id)

        if request.method == 'POST':
            # Assuming you have a form field for payment method
            payment_method = request.POST.get('payment_method')

            # Calculate the payment amount based on the booking's total price
            payment_amount = booking.calculate_total_price()

            # Create a Payment instance
            payment = Payment.create_payment(
                room_booking=booking,
                payment_amount=payment_amount,
                payment_method=payment_method
            )

            # Customize the logic here, e.g., redirect to a success page
            return render(request, 'payments/payment_success.html', {'payment': payment})

        # Render the payment form with the booking details
        return render(request, 'payments/index.html', {'booking': booking, 'total_price': booking.total_price})

    except HotelBooking.DoesNotExist:
        # Handle the case where the booking is not found
        return render(request, 'error.html', {'error_message': 'Booking not found'}, status=404)
