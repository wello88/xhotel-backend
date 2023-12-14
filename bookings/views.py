from rest_framework.response import Response
from rest_framework import status
from .serializers import HotelBookingSerializer
from rest_framework import generics
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import HotelBooking,Room
from .serializers import HotelBookingSerializer
from rest_framework.authentication import TokenAuthentication


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class HotelBookingListCreateView(generics.ListCreateAPIView):
    queryset = HotelBooking.objects.all()
    serializer_class = HotelBookingSerializer
    permission_classes = [IsAuthenticated]  

#     def create(self, request, *args, **kwargs):
#         # Validate the token
#         if not request.auth:
#             return Response({'error': 'Authentication credentials not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

#         # Extract the user from the token
#         user = request.user

#         # Check if the user has write access
#         if not user.has_perm('booking.add_hotelbooking'):
#             return Response({'error': 'Insufficient permissions.'}, status=status.HTTP_403_FORBIDDEN)

#         # Extract room_id, check_in_date, and check_out_date from the request data
#           # Customize create behavior to associate the booking with the correct room
#         # room_id = request.data.get('room')
#         # room = Room.objects.get(room_id=room_id)
#         # request.data['room'] = room.id
#         check_in_date = request.data.get('check_in_date')
#         check_out_date = request.data.get('check_out_date')

#         # Check if the room exists
#         # try:
#         #     room = Room.objects.get(room_id=room_id)
#         # except Room.DoesNotExist:
#         #     return Response({'error': 'Room does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

#         # You can add more validation checks here if needed

#         # Create a hotel booking
#         booking_data = {
#             # 'room_id': room_id,
#             'check_in_date': check_in_date,
#             'check_out_date': check_out_date,
#         }
#         serializer = HotelBookingSerializer(data=booking_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        # Get the default list response
        response = super().list(request, *args, **kwargs)

        # Customize the response data to include check-in and check-out dates in an array
        data = response.data
        custom_data = []

        for booking_data in data:
            check_in_date = booking_data.get('check_in_date')
            check_out_date = booking_data.get('check_out_date')
            date_array = [check_in_date, check_out_date]
            custom_data.append({
                **booking_data,
                'date_array': date_array,
            })

        response.data = custom_data

        return response

    def create(self, request, *args, **kwargs):
        # Validate the token
        if not request.auth:
            return Response({'error': 'Authentication credentials not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Extract the user from the token
        user = request.user  # Access user directly from the request

        # Check if the user has write access
        if not user.has_perm('booking.add_hotelbooking'):
            return Response({'error': 'Insufficient permissions.'}, status=status.HTTP_403_FORBIDDEN)
        # Customize create behavior if needed
        return super().create(request, *args, **kwargs)



