from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.models import CustomUser  # Import CustomUser model from accounts app
from .serializers import CustomUserSerializer
from bookings.serializers import HotelBookingSerializer
from bookings.models import HotelBooking

class ProfileDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        custom_user = CustomUser.objects.get(pk=user.pk)
        serializer_user = CustomUserSerializer(custom_user)

        # Retrieve booking data for the user from HotelBooking model
        bookings = HotelBooking.objects.filter(user=user)
        serializer_bookings = HotelBookingSerializer(bookings, many=True)

        return Response({
            'user_data': serializer_user.data,
            'bookings': serializer_bookings.data
        })