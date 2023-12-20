# # bookings/utils.py

# from .models import HotelBooking
# import math

# def calculate_price(booking):
#     # Assuming you have a related hotel in your HotelBooking model
#     original_price = HotelBooking.hotel.price

#     room = HotelBooking.room_count
#     adult = HotelBooking.adult_count
#     child = HotelBooking.child_count
#     days = (HotelBooking.check_out_date - HotelBooking.check_in_date).days + 1

#     # Example calculation logic
#     price = original_price * room
#     price += math.floor(original_price * (adult - 1) * 0.5)
#     price += math.floor(original_price * child / 4)
#     price += math.floor(original_price * (days - 1) / 3)

#     return price
