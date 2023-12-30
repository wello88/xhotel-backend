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

# class HotelBookingListCreateView(generics.ListCreateAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = HotelBooking.objects.all()
#     serializer_class = HotelBookingSerializer

#     def list(self, request, *args, **kwargs):
#         response = super().list(request, *args, **kwargs)
#         data = response.data

#         custom_data = [
#             {**booking_data, 'date_array': [booking_data.get('check_in_date'), booking_data.get('check_out_date')]}
#             for booking_data in data
#         ]

#         response.data = custom_data
#         return response
#     def create(self, request, *args, **kwargs):
#         if not request.auth:
#             return Response({'error': 'Authentication credentials not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

#         user = request.user

#         if not user.has_perm('booking.add_hotelbooking'):
#             return Response({'error': 'Insufficient permissions.'}, status=status.HTTP_403_FORBIDDEN)

#         # Extract relevant data from the request
#         room_id = request.data.get('room')
#         check_in_date = request.data.get('check_in_date')
#         check_out_date = request.data.get('check_out_date')

#         # Check if there are any overlapping bookings for the specified room and time period
#         existing_bookings = HotelBooking.objects.filter(
#             room=room_id,
#             check_out_date__gt=check_in_date,
#             check_in_date__lt=check_out_date
#         )

#         if existing_bookings.exists():
#             return Response({'error': 'The room is already booked for the specified time period.'}, status=status.HTTP_400_BAD_REQUEST)

#         return super().create(request, *args, **kwargs)





















from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import HotelBooking, Room
from .serializers import HotelBookingSerializer

# class HotelBookingListCreateView(generics.ListCreateAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = HotelBooking.objects.all()
#     serializer_class = HotelBookingSerializer

#     def list(self, request, *args, **kwargs):
#         response = super().list(request, *args, **kwargs)
#         data = response.data

#         custom_data = [
#             {**booking_data, 'date_array': [booking_data.get('check_in_date'), booking_data.get('check_out_date')]}
#             for booking_data in data
#         ]

#         response.data = custom_data
#         return response

#     def create(self, request, *args, **kwargs):
#         print("777777777777777")
#         if not request.auth:
#             return Response({'error': 'Authentication credentials not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

#         user = request.user
#         print(user.id)
#         if not user.has_perm('booking.add_hotelbooking'): 
#             return Response({'error': 'Insufficient permissions.'}, status=status.HTTP_403_FORBIDDEN)

#         # Extract relevant data from the request
#         room_id = request.data.get('room')
#         check_in_date = request.data.get('check_in_date')
#         check_out_date = request.data.get('check_out_date')
#         numberOfAdults = request.data.get('adults', 0)
#         numberOfKids = request.data.get('kids', 0)

#         # Retrieve the room details
#         room = Room.objects.get(pk=room_id)

#         # Check if there are any overlapping bookings for the specified room and time period
#         existing_bookings = HotelBooking.objects.filter(
#             room=room_id,
#             check_out_date__gt=check_in_date,
#             check_in_date__lt=check_out_date
#         )

#         if existing_bookings.exists():
#             return Response({'error': 'The room is already booked for the specified time period.'}, status=status.HTTP_400_BAD_REQUEST)

#         # Calculate the price for the room
#         numberOfDays = (check_out_date - check_in_date).days
#         room_price = room.room_price
#         total_price = room_price * numberOfDays * (1 + 0.2 * numberOfAdults + 0.1 * numberOfKids)

#         # Add the calculated price to the request data
#         request.data['total_price'] = total_price

#         return super().create(request, *args, **kwargs)






# from datetime import datetime
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import generics
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from .models import HotelBooking, Room
# from .serializers import HotelBookingSerializer

# from rest_framework import generics, permissions, status
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.response import Response
# from .models import HotelBooking
# from .serializers import HotelBookingSerializer
# from bookings.models import Room
# from datetime import timedelta

# class HotelBookingListCreateView(generics.ListCreateAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = HotelBooking.objects.all()
#     serializer_class = HotelBookingSerializer

#     def list(self, request, *args, **kwargs):
#         response = super().list(request, *args, **kwargs)
#         data = response.data

#         custom_data = [
#             {**booking_data, 'date_array': [booking_data.get('check_in_date'), booking_data.get('check_out_date')]}
#             for booking_data in data
#         ]

#         response.data = custom_data
#         return response

#     def create(self, request, *args, **kwargs):
#         print("777777777777777")
#         if not request.auth:
#             return Response({'error': 'Authentication credentials not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

#         user = request.user
#         print(user.id)

#         if not user.has_perm('booking.add_hotelbooking'): 
#             return Response({'error': 'Insufficient permissions.'}, status=status.HTTP_403_FORBIDDEN)

#         room_id = request.data.get('room')
#      # Convert date strings to datetime.date objects
#         check_in_date = datetime.strptime(request.data.get('check_in_date'), '%Y-%m-%d').date()
#         check_out_date = datetime.strptime(request.data.get('check_out_date'), '%Y-%m-%d').date()
#         numberOfAdults = request.data.get('adults', 0)
#         numberOfKids = request.data.get('kids', 0)

#         # Retrieve the room details
#         room = Room.objects.get(pk=room_id)

#         # Check if there are any overlapping bookings for the specified room and time period
#         existing_bookings = HotelBooking.objects.filter(
#             room=room_id,
#             check_out_date__gt=check_in_date,
#             check_in_date__lt=check_out_date
#         )

#         if existing_bookings.exists():
#             return Response({'error': 'The room is already booked for the specified time period.'}, status=status.HTTP_400_BAD_REQUEST)

#         # Convert relevant variables to numeric types
#         room_price = float(room.room_price)
#         numberOfDays = int((check_out_date - check_in_date).days)
#         numberOfAdults = int(numberOfAdults)
#         numberOfKids = int(numberOfKids)

#         # Calculate the price for the room
#         total_price = room_price * numberOfDays * (1 + 0.2 * numberOfAdults + 0.1 * numberOfKids)
#         user.id
#         # Add the calculated price to the request data
#         request.data['total_price'] = total_price

#         return super().create(request, *args, **kwargs)























from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime
from .models import HotelBooking
from .models import HotelBooking, Room
from .serializers import HotelBookingSerializer

class HotelBookingListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
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
        print("777777777777777")
        if not request.auth:
            return Response({'error': 'Authentication credentials not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

        room_id = request.data.get('room')
        check_in_date = datetime.strptime(request.data.get('check_in_date'), '%Y-%m-%d').date()
        check_out_date = datetime.strptime(request.data.get('check_out_date'), '%Y-%m-%d').date()
        numberOfAdults = request.data.get('adults', 0)
        numberOfKids = request.data.get('kids', 0)

        room = Room.objects.get(pk=room_id)

        existing_bookings = HotelBooking.objects.filter(
            room=room_id,
            check_out_date__gt=check_in_date,
            check_in_date__lt=check_out_date
        )

        if existing_bookings.exists():
            return Response({'error': 'The room is already booked for the specified time period.'}, status=status.HTTP_400_BAD_REQUEST)

        room_price = float(room.room_price)
        numberOfDays = int((check_out_date - check_in_date).days)
        numberOfAdults = int(numberOfAdults)
        numberOfKids = int(numberOfKids)

        total_price = room_price * numberOfDays * (1 + 0.2 * numberOfAdults + 0.1 * numberOfKids)

        request.data['total_price'] = total_price

        return super().create(request, *args, **kwargs)




















































# Code DashBoard For Reviews & user_booked & Hotels
from rest_framework import generics, status
from rest_framework.response import Response
from review.models import Review
from bookings.models import HotelBooking, Hotel

class RoomBookingView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = HotelBookingSerializer  # Use the serializer for Room model

    def list(self, request, *args, **kwargs):
        review_count = Review.objects.count()
        user_booked_count = HotelBooking.objects.count()
        hotel_count = Hotel.objects.count() 

        response_data = [{
            'review_count': review_count,
            'user_booked_count': user_booked_count,
            'hotel_count': hotel_count
        }]

        data = {'counts': response_data}
        return Response(data, status=status.HTTP_200_OK)







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


from django.urls import path




















# import math
# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# from rest_framework import generics, status
# from rest_framework.response import Response
# from .models import Hotel, HotelBooking, Room
# from .serializers import HotelBookingSerializer
# from django.shortcuts import render, get_object_or_404
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework import status

# class HotelBookingListCreateView(generics.ListCreateAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = HotelBooking.objects.all()
#     serializer_class = HotelBookingSerializer

#     def list(self, request, *args, **kwargs):
#         response = super().list(request, *args, **kwargs)
#         data = response.data

#         custom_data = [
#             {**booking_data, 'date_array': [booking_data.get('check_in_date'), booking_data.get('check_out_date')]}
#             for booking_data in data
#         ]

#         response.data = custom_data
#         return response
#     def post(self, request, *args, **kwargs):
#         print("welcome")
#         if not request.auth:
#             return Response({'error': 'Authentication credentials not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

#         user = request.user
#         print(user.id)
#         if not user.has_perm('booking.add_hotelbooking'):
#             return Response({'error': 'Insufficient permissions.'}, status=status.HTTP_403_FORBIDDEN)

#         # Extract relevant data from the request
#         # user=user,
#         room_id = request.data.get('room')
#         check_in_date = request.data.get('check_in_date')
#         check_out_date = request.data.get('check_out_date')
#         # Check if there are any overlapping bookings for the specified room and time period
#         existing_bookings = HotelBooking.objects.filter(
#             # uerId=1,
#             room=room_id,
#             check_out_date__gt=check_in_date,
#             check_in_date__lt=check_out_date
#         )

#         if existing_bookings.exists():
#             return Response({'error': 'The room is already booked for the specified time period.'}, status=status.HTTP_400_BAD_REQUEST)

#         return super().create(request, *args, **kwargs)
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









































# Code DashBoard For Reviews & user_booked & Hotels
from rest_framework import generics, status
from rest_framework.response import Response
from review.models import Review
from bookings.models import HotelBooking, Hotel

class RoomBookingView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = HotelBookingSerializer  # Use the serializer for Room model

    def list(self, request, *args, **kwargs):
        review_count = Review.objects.count()
        user_booked_count = HotelBooking.objects.count()
        hotel_count = Hotel.objects.count()

        response_data = [{
            'review_count': review_count,
            'user_booked_count': user_booked_count,
            'hotel_count': hotel_count
        }]

        data = {'counts': response_data}
        return Response(data, status=status.HTTP_200_OK)




















































from django.http import JsonResponse
from .models import HotelBooking

def count_users_booked_hotel(request):
    user_counts = (
        HotelBooking.objects.count()
    )

    user_counts_array = [{"number_of_users_booked": [user_counts]}]

    return JsonResponse(user_counts_array, safe=False)
































from django.shortcuts import get_object_or_404
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from bookings.models import HotelBooking  # تحديث مسار استيراد نموذج HotelBooking بناءً على هيكل المشروع الخاص بك

@login_required
def get_user_booking_info(request):
    registration_code = request.user.registration.registration_code

    user = get_object_or_404(CustomUser, registration__registration_code=registration_code)

    bookings = HotelBooking.objects.filter(name=user.first_name)

    booking_info = []
    for booking in bookings:
        booking_info.append({
            'booking_id': booking.id,
            # 'room_name': booking.room.name,
            'check_in_date': booking.check_in_date,
            'check_out_date': booking.check_out_date,
            'adults': booking.adults,
            'kids': booking.kids,
            'total_price': booking.total_price,
        })

    return JsonResponse({'booking_info': booking_info})



















# views.py
# views.py

# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from .models import HotelBooking
# from accounts.models import Registration


# def get_user_booking_info_by_code(request, registration_code):
#     try:
#         # Find the registration using the registration code
#         registration = get_object_or_404(Registration, registration_code=registration_code)
#         user = registration.user

#         print(f"User: {user.username}, id: {user.id}")

#         # Find all bookings associated with the user
#         bookings = HotelBooking.objects.filter(id=user.id)

#         print(f"Number of bookings: {bookings.count()}")

#         # Aggregate booking information
#         booking_info = []
#         for booking in bookings:
#             booking_info.append({
#                 'booking_id': booking.id,
#                 # 'room_name': booking.room_name,
#                 'check_in_date': booking.check_in_date,
#                 'check_out_date': booking.check_out_date,
#                 'adults': booking.adults,
#                 'kids': booking.kids,
#                 'total_price': booking.total_price,
#             })

#         return JsonResponse({'user_info': {'username': user.username, 'id': user.id}, 'booking_info': booking_info})

#     except Registration.DoesNotExist:
#         return JsonResponse({'error': 'Registration not found.'}, status=404)










# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from accounts.models import CustomUser
# from .models import HotelBooking

# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def get_user_booking_info(request):
#     if not request.user.is_authenticated:
#         print("User not authenticated")
#         return JsonResponse({'error': 'Authentication credentials not provided.'}, status=401)

#     # Assuming the access token is not needed with TokenAuthentication

#     # Extract the registration code from the user (adjust as per your user model structure)
#     registration_code = request.user.registration.registration_code if hasattr(request.user, 'registration') else None

#     if not registration_code:
#         return JsonResponse({'error': 'User registration information not found.'}, status=404)

#     # Find the user using the registration code
#     user = get_object_or_404(CustomUser, registration__registration_code=registration_code)

#     # Find all bookings associated with the user
#     bookings = HotelBooking.objects.filter(room__hotel=user.hotel)

#     # Aggregate booking information
#     booking_info = []
#     for booking in bookings:
#         booking_info.append({
#             'booking_id': booking.id,
#             'room_name': booking.room.name,
#             'check_in_date': booking.check_in_date,
#             'check_out_date': booking.check_out_date,
#             'adults': booking.adults,
#             'kids': booking.kids,
#             'total_price': booking.total_price,
#         })

#     return JsonResponse({'booking_info': booking_info})




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






# from django.http import JsonResponse
# from .models import Room

# def get_all_rooms(request):
#     all_rooms = Room.objects.all()

#     # Serialize the data if needed (convert it to JSON for instance)
#     serialized_rooms = [{'room_id': room.room_id, 'room_type': room.room_type} for room in all_rooms]

#     # Return the serialized data as a JSON response
#     return JsonResponse({'rooms': serialized_rooms}, safe=False)

from django.http import JsonResponse
from .models import Room

def get_all_rooms(request):
    all_rooms = Room.objects.all()

    # Serialize the data including the required fields
    serialized_rooms = [
        {
            'room_type': room.room_type,
            'hotel': room.hotel.name,
            'room_id': room.room_id,
            'room_name': room.room_name,
            'room_price': room.room_price,
            # 'room_image':room.room_image,
        }
        for room in all_rooms
    ]

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












from rest_framework import generics
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSearchSerializer

class RoomSearchView(generics.ListAPIView):
    serializer_class = RoomSearchSerializer

    def get_queryset(self):
        # Retrieve query parameters from the request


            # 'room_type': room.room_type,
            # 'hotel': room.hotel.name,
            # 'room_id': room.room_id,
            # 'room_name': room.room_name,
            # 'room_price': room.room_price,

        room_type = self.request.query_params.get('room_type', None)
        room_name = self.request.query_params.get('room_name', None)
        room_id = self.request.query_params.get('room_id', None)

        # Filter rooms based on the provided criteria
        queryset = Room.objects.all()

        # if room_type:
            # queryset = queryset.filter(room_type=room_type)

        if room_name:
            queryset = queryset.filter(room_name=room_name)

        # if room_id:
        #     queryset = queryset.filter(room_pricelte=room_id)
            return queryset