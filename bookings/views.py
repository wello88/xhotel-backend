from rest_framework import generics
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from accounts.models import CustomUser 
from .models import HotelBooking
from .serializers import HotelBookingSerializer




@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class HotelBookingListCreateView(generics.ListCreateAPIView):
    queryset = HotelBooking.objects.all()
    serializer_class = HotelBookingSerializer
    permission_classes = [IsAuthenticated]  # Use TokenHasReadWritePermission

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
        user_id = request.auth.get('user_id')
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Check if user has write access
        if not user.has_perm('booking.add_hotelbooking'):
            return Response({'error': 'Insufficient permissions.'}, status=status.HTTP_403_FORBIDDEN)

        # # Continue with the booking creation logic
        # Customize create behavior if needed
        return super().create(request, *args, **kwargs)


