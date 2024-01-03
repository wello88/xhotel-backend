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

# # @login_required
# def get_user_booking_info(request):
#     if request.user and request.user.registration:
#         registration_code = request.user.registration.registration_code
#     else:
#     # Handle the case where registration is None
#         return JsonResponse({'error': 'User registration information not found.'}, status=404)
#     user = get_object_or_404(CustomUser, registration__registration_code=registration_code)

#     bookings = HotelBooking.objects.filter(name=user.first_name)

#     booking_info = []
#     for booking in bookings:
#         booking_info.append({
#             'booking_id': booking.id,
#             # 'room_name': booking.room.name,
#             'check_in_date': booking.check_in_date,
#             'check_out_date': booking.check_out_date,
#             'adults': booking.adults,
#             'kids': booking.kids,
#             'total_price': booking.total_price,
#         })

#     return JsonResponse({'booking_info': booking_info})




















from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.shortcuts import get_object_or_404
from accounts.models import CustomUser
from bookings.models import HotelBooking
from django.http import JsonResponse

class UserBookingInfoAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        registration_code = self.request.user.registration.registration_code
        user = get_object_or_404(CustomUser, registration__registration_code=registration_code)

        bookings = HotelBooking.objects.filter(name=user.first_name)

        booking_info = []
        for booking in bookings:
            booking_info.append({
                'booking_id': booking.id,
                'check_in_date': booking.check_in_date,
                'check_out_date': booking.check_out_date,
                'adults': booking.adults,
                'kids': booking.kids,
                'total_price': booking.total_price,
            })

        return Response({'booking_info': booking_info})




















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