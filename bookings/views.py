# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import HotelBookingSerializer
# from rest_framework import generics
# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework import status
# from .models import HotelBooking,Room
# from .serializers import HotelBookingSerializer
# from rest_framework.authentication import TokenAuthentication
from django.urls import path
# import math


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# class HotelBookingListCreateView(generics.ListCreateAPIView):
#     queryset = HotelBooking.objects.all()
#     serializer_class = HotelBookingSerializer
#     permission_classes = [IsAuthenticated]  

# #     def create(self, request, *args, **kwargs):
# #         # Validate the token
# #         if not request.auth:
# #             return Response({'error': 'Authentication credentials not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

# #         # Extract the user from the token
# #         user = request.user

# #         # Check if the user has write access
# #         if not user.has_perm('booking.add_hotelbooking'):
# #             return Response({'error': 'Insufficient permissions.'}, status=status.HTTP_403_FORBIDDEN)

# #         # Extract room_id, check_in_date, and check_out_date from the request data
# #           # Customize create behavior to associate the booking with the correct room
# #         # room_id = request.data.get('room')
# #         # room = Room.objects.get(room_id=room_id)
# #         # request.data['room'] = room.id
# #         check_in_date = request.data.get('check_in_date')
# #         check_out_date = request.data.get('check_out_date')

# #         # Check if the room exists
# #         # try:
# #         #     room = Room.objects.get(room_id=room_id)
# #         # except Room.DoesNotExist:
# #         #     return Response({'error': 'Room does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

# #         # You can add more validation checks here if needed

# #         # Create a hotel booking
# #         booking_data = {
# #             # 'room_id': room_id,
# #             'check_in_date': check_in_date,
# #             'check_out_date': check_out_date,
# #         }
# #         serializer = HotelBookingSerializer(data=booking_data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         else:
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def list(self, request, *args, **kwargs):
#         # Get the default list response
#         response = super().list(request, *args, **kwargs)

#         # Customize the response data to include check-in and check-out dates in an array
#         data = response.data
#         custom_data = []

#         for booking_data in data:
#             check_in_date = booking_data.get('check_in_date')
#             check_out_date = booking_data.get('check_out_date')
#             date_array = [check_in_date, check_out_date]
#             custom_data.append({
#                 **booking_data,
#                 'date_array': date_array,
#             })

#         response.data = custom_data

#         return response

#     def create(self, request, *args, **kwargs):
#         # Validate the token
#         if not request.auth:
#             return Response({'error': 'Authentication credentials not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

#         # Extract the user from the token
#         user = request.user  # Access user directly from the request

#         # Check if the user has write access
#         if not user.has_perm('booking.add_hotelbooking'):
#             return Response({'error': 'Insufficient permissions.'}, status=status.HTTP_403_FORBIDDEN)
#         # Customize create behavior if needed
#         return super().create(request, *args, **kwargs)
































































import math
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Hotel, HotelBooking, Room
from .serializers import HotelBookingSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

class HotelBookingListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = HotelBooking.objects.all()
    serializer_class = HotelBookingSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        data = response.data

        custom_data = [
            {**booking_data, 'date_array': [booking_data.get('check_in_date'), booking_data.get('check_out_date')]}
            for booking_data in data
        ]

        response.data = custom_data
        return response
    def create(self, request, *args, **kwargs):
        if not request.auth:
            return Response({'error': 'Authentication credentials not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

        user = request.user

        if not user.has_perm('booking.add_hotelbooking'):
            return Response({'error': 'Insufficient permissions.'}, status=status.HTTP_403_FORBIDDEN)

        # Extract relevant data from the request
        room_id = request.data.get('room')
        check_in_date = request.data.get('check_in_date')
        check_out_date = request.data.get('check_out_date')

        # Check if there are any overlapping bookings for the specified room and time period
        existing_bookings = HotelBooking.objects.filter(
            room=room_id,
            check_out_date__gt=check_in_date,
            check_in_date__lt=check_out_date
        )

        if existing_bookings.exists():
            return Response({'error': 'The room is already booked for the specified time period.'}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
    # def create(self, request, *args, **kwargs):
    #     if not request.auth:
    #         return Response({'error': 'Authentication credentials not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

    #     user = request.user

    #     if not user.has_perm('booking.add_hotelbooking'):
    #         return Response({'error': 'Insufficient permissions.'}, status=status.HTTP_403_FORBIDDEN)

    #     room_id = request.data.get('room')
    #     room_type = request.data.get('room_type')

    #     # Check if the user already has a booking for the same room and type
    #     existing_booking = HotelBooking.objects.filter(user=user, room=room_id, room_type=room_type).exists()

    #     if existing_booking:
    #         return Response({'error': 'You have already booked the same room at the same type.'}, status=status.HTTP_400_BAD_REQUEST)

    #     return super().create(request, *args, **kwargs)

    
#     def get_room_details(self, room_id):
#         try:
#             room = Room.objects.get(id=room_id)
#             return {'status': room.status, 'room_type': room.room_type}
#         except Room.DoesNotExist:
#             return {'status': None, 'room_type': None}

# def count_users_booked_hotel(request):
#     user_counts = HotelBooking.objects.count()
#     user_counts_array = [{"number_of_users_booked": user_counts}]
#     return JsonResponse(user_counts_array, safe=False)

# def count_hotels(request):
#     hotel_count = Hotel.objects.count()
#     hotel_count_array = [{"number_of_hotels": hotel_count}]
#     return JsonResponse(hotel_count_array, safe=False)

# def count_rooms(request):
#     room_count = Room.objects.count()
#     room_count_array = [{"number_of_rooms_booked": room_count}]
#     return JsonResponse(room_count_array, safe=False)

# def create_price(id, room, adult, child, days):
#     original_price = Hotel.objects.get(id=id).price
#     price = original_price * room
#     price += math.floor(original_price * (adult - 1) * 0.5)
#     price += math.floor(original_price * child / 4)
#     price += math.floor(original_price * (days - 1) / 3)
#     return price

# def get_hotel_details(request):
#     hotels = Hotel.objects.all()
#     hotel_details = [{'name': hotel.name, 'average_price': str(hotel.average_price) if hotel.average_price else None, 'location': hotel.location if hotel.location else None} for hotel in hotels]
#     return JsonResponse({'hotels': hotel_details})

# def get_all_rooms(request):
#     all_rooms = Room.objects.all()
#     serialized_rooms = [{'room_id': room.room_id, 'room_type': room.room_type, 'status': room.status} for room in all_rooms]
#     return JsonResponse({'rooms': serialized_rooms}, safe=False)

# def book_hotel(request):
#     if request.method != "POST":
#         return JsonResponse({"error": "Page does not exist"}, status=404)

#     room_id = int(request.POST.get("room", 0))  # Default to 0 if not provided
#     adult = int(request.POST.get("adult", 0))
#     child = int(request.POST.get("child", 0))
#     days = int(request.POST.get("days", 0))
#     hotel_id = int(request.POST.get("id", 0))  # Assuming you are trying to get the hotel ID
#     checkin = request.POST.get("checkin", "")
#     checkout = request.POST.get("checkout", "")

#     room = get_object_or_404(Room, room_id=room_id)

#     price = create_price(hotel_id, room, adult, child, days)
    
#     hotel = get_object_or_404(Hotel, id=hotel_id)

#     response_data = {
#         "price": price,
#         "hotel": {"name": hotel.name, "location": hotel.location},
#         "room": {"room_id": room.room_id, "room_type": room.room_type, "status": room.status},
#         "adult": adult,
#         "child": child,
#         "checkin": checkin,
#         "checkout": checkout,
#         "days": days,
#     }

#     return JsonResponse(response_data)






























































































from django.http import JsonResponse
from .models import HotelBooking

def count_users_booked_hotel(request):
    user_counts = (
        HotelBooking.objects.count()
    )

    user_counts_array = [{"number_of_users_booked": [user_counts]}]

    return JsonResponse(user_counts_array, safe=False)
















# views.py

from django.http import JsonResponse
from .models import Hotel

def count_hotels(request):
    hotel_count = Hotel.objects.count()
    hotel_count_array = [{"number_of_hotels": [hotel_count]}]
    return JsonResponse(hotel_count_array, safe=False)





# views.py_count

from django.http import JsonResponse
from .models import Room  # Import the Room model

def count_rooms(request):
    room_count = Room.objects.count()
    room_count_array = [{"number_of_rooms": [room_count]}]
    return JsonResponse(room_count_array, safe=False)






from django.http import JsonResponse
from .models import Room

def get_all_rooms(request):
    all_rooms = Room.objects.all()

    # Serialize the data if needed (convert it to JSON for instance)
    serialized_rooms = [{'room_id': room.room_id, 'room_type': room.room_type, 'status': room.status} for room in all_rooms]

    # Return the serialized data as a JSON response
    return JsonResponse({'rooms': serialized_rooms}, safe=False)


# # # باختصار، تقوم الوظيفة بحساب السعر الإجمالي لحجز غرفة في فندق باستخدام التكلفة الأساسية (عدد الغرف)،
# #  وتكاليف إضافية للبالغين والأطفال، 
# #  وتكاليف تعتمد على مدة الإقامة. يتم استخدام 
# # math.floor لتقريب القيم إلى أقرب عدد صحيح.
# def create_price(id, room, adult, child, days):
#     original_price = Hotel.objects.get(id=id).price
#     price = original_price * room
#     price += math.floor(original_price * (adult - 1) * 0.5)
#     price += math.floor(original_price * child / 4)
#     price += math.floor(original_price * (days - 1) / 3)
#     return price




from .models import Hotel
from django.http import JsonResponse

def get_hotel_details(request):
    hotels = Hotel.objects.all()

    hotel_details = []
    for hotel in hotels:
        hotel_details.append({
            'name': hotel.name,
            'average_price': str(hotel.average_price) if hotel.average_price else None,
            'location': hotel.location if hotel.location else None
        })

    return JsonResponse({'hotels': hotel_details})
path('hotel-details/', get_hotel_details, name='hotel-details'),















# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import HotelBooking
# # from .utils import calculate_price

# class CalculatePriceView(APIView):
#     def get(self, request, booking_id):
#         # Get the Booking instance
#         booking = get_object_or_404(HotelBooking, pk=booking_id)

#         # Calculate the price
#         total_price = calculate_price(booking)

#         # Do something with the calculated price (e.g., return it in an API response)
#         return Response({'total_price': total_price})