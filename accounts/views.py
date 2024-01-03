# views.py
#registeration
from rest_framework.decorators import permission_classes, authentication_classes
from django.contrib.auth import get_user_model
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from allauth.account.utils import send_email_confirmation
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserSerializer




User = get_user_model()

class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Create user instance but don't save it yet
        user = serializer.save()

        # Set user as inactive until email confirmation
        user.is_active = False
        user.save(update_fields=['is_active'])  # Update only 'is_active' field

        # Send an email confirmation to the user's email address
        send_email_confirmation(request, user)

        # refresh = RefreshToken.for_user(User.objects.get(username=user.username))
        # access_token = str(refresh.access_token)

        headers = self.get_success_headers(serializer.data)
        return Response({'detail': 'Please confirm your email address to complete the registration.',
                         },
                        status=status.HTTP_201_CREATED, headers=headers)





#login
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.tokens import default_token_generator 


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # Check if the user has confirmed their email
        username = request.data.get('username')
        user = get_user_model().objects.get(username=username)
        email_address = EmailAddress.objects.get(user=user, verified=True)

        if email_address:
            # User has confirmed their email, provide access and refresh tokens
            refresh_token = self.get_refresh_token(user)
            access_token = str(refresh_token.access_token)
            token_key = response.data['access']
            
            return JsonResponse({
                'access_token': access_token,
                'refresh_token': str(refresh_token),
                'token_key': token_key,  # The actual token key
                'detail': 'Login successful.'
            }, status=response.status_code)



    def get_refresh_token(self, user):
        refresh = default_token_generator.make_token(user)
        refresh_token = RefreshToken.for_user(user)
        refresh_token.access_token.payload['refresh'] = refresh
        return refresh_token



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout

class LogoutAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            # Log out the currently authenticated user
            logout(request)
            return Response({"detail": "Logout successful."}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"detail": "An error occurred during logout."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)








#     # accounts/views.py/logout
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import IsAuthenticated

# class LogoutAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         try:
#             # Get the refresh token from the request headers
#             refresh_token = request.headers.get('Authorization').split(' ')[1]

#             # Use the refresh token to get the user and blacklist it
#             user = request.user
#             refresh = RefreshToken.for_user(user)
#             access_token_payload = refresh.access_token.payload

#             if access_token_payload['jti'] == refresh_token:
#                 refresh.blacklist()
#                 return Response({"detail": "Logout successful."}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)

#         except Exception as e:
#             return Response({"detail": "Invalid token or token not provided."}, status=status.HTTP_400_BAD_REQUEST)

# accounts/views.py/changepass

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import update_session_auth_hash
from .serializers import ChangePasswordSerializer

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)  # To update session after password change
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










#admin
from admin_user.models import Programs
from django.http import JsonResponse

def get_hopiees(request):
    # Fetch all Programs from the database
    hopiees = Programs.objects.all()

    # Serialize the data if needed (convert it to JSON for instance)
    serialized_hopiees = []
    for hopiee in hopiees:
        serialized_hopiees.append({
            'days': hopiee.days,
            'nights': hopiee.nights,
            'massage': hopiee.massage,
            'safari': hopiee.safari,
            'camping': hopiee.camping,
            'seatrip': hopiee.seatrip,
            'diving': hopiee.diving,
            'snorkeling': hopiee.snorkeling,
        })

    # Return the serialized data as a JSON response
    return JsonResponse({'hopiees': serialized_hopiees})


#get data 
from admin_user.models import Programs
from django.http import JsonResponse

def get_programs_data(request):
    programs_data = Programs.objects.all().values()  # Retrieve all data from Programs table
    return JsonResponse(list(programs_data), safe=False)





from django.http import JsonResponse
from .models import CustomUser

def get_all_user_hobbies(request):
    all_user_hobbies = CustomUser.objects.values_list('hobbies', flat=True)
    return JsonResponse({"hobbies": list(all_user_hobbies)})




# views.py_count

from django.http import JsonResponse
from .models import CustomUser  # Import the CustomUser model

def count_custom_users(request):
    custom_user_count = CustomUser.objects.count()
    custom_user_count_array = [{"number_of_custom_users":[custom_user_count]}]
    return JsonResponse(custom_user_count_array, safe=False)




#what email user has register by
from .models import CustomUser
from django.http import JsonResponse

def get_user_email(user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        user_email = user.email
        return user_email
    except CustomUser.DoesNotExist:
        return None  # Return None if the user doesn't exist

def get_email_by_user_id(request):
    # Assuming you receive the user ID via a GET or POST request parameter
    user_id = request.GET.get('user_id')  # Modify this according to your request method

    if not user_id:
        return JsonResponse({'error': 'User ID parameter missing'}, status=400)

    user_email = get_user_email(user_id)

    if user_email:
        return JsonResponse({'email': user_email})
    else:
        return JsonResponse({'error': 'User not found'}, status=404)

















