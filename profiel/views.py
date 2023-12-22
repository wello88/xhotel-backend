# # profiel/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from accounts.models import CustomUser
# from .serializers import CustomUserSerializer
# from bookings.serializers import HotelBookingSerializer
# from bookings.models import HotelBooking

# class ProfileDetailView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request,username):
#         # user = request.user
#         user = request.user  # Retrieve the authenticated user from the request
#         serializer_user = CustomUserSerializer(user)

#         # Retrieve booking data for the user from HotelBooking model
#         bookings = HotelBooking.objects.filter(user=user)
#         serializer_bookings = HotelBookingSerializer(bookings, many=True)

#         # Create a response dictionary with "user_data" and "bookings" as lists
#         response_data = {
#             "user_data": [{
#                 # "id": serializer_user.data["id"],
#                 "username": serializer_user.data["username"],
#                 "email": serializer_user.data["email"],
#             }],
#              'bookings': serializer_bookings.data
#         }

#         return Response(response_data)

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.models import CustomUser  # Import CustomUser model from accounts app
from .serializers import CustomUserSerializer
from bookings.serializers import HotelBookingSerializer
from bookings.models import HotelBooking

# # class ProfileDetailView(APIView):
# #     authentication_classes = [JWTAuthentication]
# #     permission_classes = [IsAuthenticated]

# #     def get(self, request):
# #         user = request.user
# #         custom_user = CustomUser.objects.get(pk=user.pk)
# #         serializer_user = CustomUserSerializer(custom_user)

# #         # Retrieve booking data for the user from HotelBooking model
# #         bookings = HotelBooking.objects.filter(user=user)
# #         serializer_bookings = HotelBookingSerializer(bookings, many=True)

# #         return Response({
# #             'user_data': serializer_user.data,
# #             'bookings': serializer_bookings.data
# #         })







# # profiel/views.py

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from accounts.models import CustomUser
# from .serializers import CustomUserSerializer
# from bookings.serializers import HotelBookingSerializer
# from bookings.models import HotelBooking
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .serializers import CustomUserSerializer
# from bookings.models import HotelBooking  

# class ProfileDetailView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         user = request.user
#         custom_user = CustomUser.objects.get(pk=user.pk)
#         serializer_user = CustomUserSerializer(custom_user)

#         # Retrieve booking data for the user from HotelBooking model
#         bookings = HotelBooking.objects.filter(user=user)
#         serializer_bookings = HotelBookingSerializer(bookings, many=True)

#         # Create a response dictionary with "user_data" and "bookings" as lists
#         response_data = {
#             "user_data": [{
#                 # "id": serializer_user.data["id"],
#                 "username": serializer_user.data["username"],
#                 "email": serializer_user.data["email"],
#             }],
#             'bookings': serializer_bookings.data
#         }

#         return Response(response_data)





































































from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import CustomUserSerializer

User = get_user_model()

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class UserProfileAPIView(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer

    def retrieve(self, request, *args, **kwargs):
        # Get the logged-in user
        user = request.user

        # Serialize user data
        serializer = self.get_serializer(user)

        # Convert serialized data to a list
        user_data_list = {"profile":[ serializer.data]}

        return Response(user_data_list, status=status.HTTP_200_OK)
















from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from bookings.models import HotelBooking
from django.shortcuts import get_object_or_404

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class UserProfileView(APIView):
    def get(self, request, *args, **kwargs):
        # Get the current user
        user = self.request.user

        # Retrieve booking data for the current user
        bookings = HotelBooking.objects.filter(room__user=user)

        # You can serialize the bookings data using Django Rest Framework serializers
        # Assuming you have a serializer for HotelBooking named HotelBookingSerializer
        serializer = HotelBookingSerializer(bookings, many=True)

        return Response(serializer.data)














# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from accounts.models import CustomUser
# from .serializers import CustomUserSerializer, HotelBookingSerializer
# from bookings.models import HotelBooking  

# class ProfileDetailView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         user = request.user
#         custom_user = CustomUser.objects.get(username=user.username)  # Use username to get the user
#         serializer_user = CustomUserSerializer(custom_user)

#         # Retrieve booking data for the user from HotelBooking model
#         bookings = HotelBooking.objects.filter(user=user)
#         serializer_bookings = HotelBookingSerializer(bookings, many=True)

#         # Create a response dictionary with "user_data" and "bookings" as lists
#         response_data = {
#             "user_data": [{
#                 "username": serializer_user.data["username"],
#                 "email": serializer_user.data["email"],
#             }],
#             'bookings': serializer_bookings.data
#         }

#         return Response(response_data)





