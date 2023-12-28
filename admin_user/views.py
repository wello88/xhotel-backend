# views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from bookings.models import Hotel, Room
from .serializers import HotelSerializer, RoomSerializer, RoomUpdateDeleteSerializer,HotelUpdateDeleteSerializer
from .permissions import IsSuperuserOrReadOnly

class HotelListCreateView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsSuperuserOrReadOnly]

class HotelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsSuperuserOrReadOnly]

    def get_serializer_class(self):
        # Use different serializer for update and delete operations
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return HotelUpdateDeleteSerializer
        return HotelSerializer

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response({"detail": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT)

class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsSuperuserOrReadOnly]

class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsSuperuserOrReadOnly]

    def get_serializer_class(self):
        # Use different serializer for update and delete operations
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return RoomUpdateDeleteSerializer
        return RoomSerializer

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response({"detail": "Successfully deleted."},status=status.HTTP_204_NO_CONTENT)



    # --------------------------------------   Retrieve the Programs object by its primary key (id)   -----------------------------------

from django.http import JsonResponse
from .models import Programs  # Import your Programs model

def get_program_by_id(request, program_id):
    try:
        # Retrieve the Programs object by its primary key (id)
        program = Programs.objects.get(pk=program_id)

        # Serialize the Programs object data if needed
        serialized_program = {
            'id': program.id,
            'days': program.days,
            'nights': program.nights,
            'massage': program.massage,
            'safari': program.safari,
            'camping': program.camping,
            'seatrip': program.seatrip,
            'diving': program.diving,
            'snorkeling': program.snorkeling,
            # Add other fields as needed
        }

        return JsonResponse(serialized_program, status=200)
    
    except Programs.DoesNotExist:
        return JsonResponse({'message': 'Program does not exist'}, status=404)

    except Exception as e:
        return JsonResponse({'message': str(e)}, status=500)
    
# --------------------------------------   Retrieve the Programs object by its primary key (id)   -----------------------------------


# views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Programs
from .serializers import ProgramsSerializer, ProgramsUpdateDeleteSerializer

class IsSuperuserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser

class ProgramsListCreateView(generics.ListCreateAPIView):
    queryset = Programs.objects.all()
    serializer_class = ProgramsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsSuperuserOrReadOnly]

class ProgramsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Programs.objects.all()
    serializer_class = ProgramsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsSuperuserOrReadOnly]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return ProgramsUpdateDeleteSerializer
        return ProgramsSerializer

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response({"detail": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
    


# yourapp/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

from .serializers import LoginSerializer

# class LoginView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']
#             user = authenticate(request, username=username, password=password)

#             if user and user.is_superuser:
#                 login(request, user)
#                 token, _ = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key})
#             else:
#                 return Response({'error': 'Invalid credentials or not a superuser.'}, status=status.HTTP_401_UNAUTHORIZED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# views.py
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

from .serializers import LoginSerializer
# views.py
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

# views.py
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

from .serializers import LoginSerializer, CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LoginView(CustomTokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = CustomTokenObtainPairSerializer(data=request.data)

        try:
            if serializer.is_valid(raise_exception=True):
                user = serializer.validated_data.get('user')
                print(f"User: {user}")

                is_superuser = getattr(user, 'is_superuser', None)
                print(f"Is Superuser: {is_superuser}")

                if is_superuser:
                    refresh = RefreshToken.for_user(user)
                    response_data = {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'details':str("login success")
                    }
                    return Response(response_data)
                else:
                    return Response({'error': 'User is not a superuser.'}, status=status.HTTP_401_UNAUTHORIZED)
        except KeyError as e:
            return Response({'error': f'Invalid credentials or missing key: {e}'}, status=status.HTTP_401_UNAUTHORIZED)
