# #register

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .serializers import UserSerializer
# from django.views.decorators.csrf import csrf_exempt

# # @csrf_exempt
# @api_view(['POST'])
# def register_user(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



#     # accounts/views.py/login

# from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from django.core.exceptions import ObjectDoesNotExist
# from rest_framework_simplejwt.tokens import RefreshToken

# from .models import CustomUser



# @api_view(['POST'])
# def user_login(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         email = request.data.get('email')
#         password = request.data.get('password')

#         user = None

#         if email:
#             try:
#                 user = CustomUser.objects.get(email=email)
#             except ObjectDoesNotExist:
#                 pass
#         elif username:
#             user = authenticate(username=username, password=password)

#         if user and user.check_password(password):
#             refresh = RefreshToken.for_user(user)
#             access_token = refresh.access_token

#             print(f"Generated Refresh Token: {str(refresh)}")
#             print(f"Generated Access Token: {str(refresh.access_token)}")

#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(access_token),
#                 'token': token.key,
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# # @api_view(['POST'])
# # def user_login(request):
# #     if request.method == 'POST':
# #         username = request.data.get('username')
# #         email=request.data.get('email')
# #         password = request.data.get('password')

# #         user = None
# #         if '@' in username:
# #             try:
# #                 user = CustomUser.objects.get(email=username)
# #             except ObjectDoesNotExist:
# #                 pass
# #         if not user:
# #             user = authenticate(username=username, password=password)
# #             if user:
# #                 refresh = RefreshToken.for_user(user)
# #                 access_token = refresh.access_token
# #             # Debug prints/logs
# #                 print(f"Generated Refresh Token: {str(refresh)}")
# #             print(f"Generated Access Token: {str(refresh.access_token)}")

# #             access_token = refresh.access_token
# #             token, _ = Token.objects.get_or_create(user=user)
# #             return Response({
# #                 'refresh': str(refresh),
# #                 'access': str(access_token),
# #                 'token': token.key,
# #             }, status=status.HTTP_200_OK)


# #         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    


#     # accounts/views.py/logout

# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def user_logout(request):
#     if request.method == 'POST':
#         try:
#             # Delete the user's token to logout
#             request.user.auth_token.delete()
#             return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


# # accounts/views.py/changepass

# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import update_session_auth_hash
# from .serializers import ChangePasswordSerializer

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def change_password(request):
#     if request.method == 'POST':
#         serializer = ChangePasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             user = request.user
#             if user.check_password(serializer.data.get('old_password')):
#                 user.set_password(serializer.data.get('new_password'))
#                 user.save()
#                 update_session_auth_hash(request, user)  # To update session after password change
#                 return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
#             return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










# #admin
# from .models import Programs
# from django.http import JsonResponse

# def get_hopiees(request):
#     # Fetch all Programs from the database
#     hopiees = Programs.objects.all()

#     # Serialize the data if needed (convert it to JSON for instance)
#     serialized_hopiees = []
#     for hopiee in hopiees:
#         serialized_hopiees.append({
#             'days': hopiee.days,
#             'nights': hopiee.nights,
#             'massage': hopiee.massage,
#             'safari': hopiee.safari,
#             'camping': hopiee.camping,
#             'seatrip': hopiee.seatrip,
#             'diving': hopiee.diving,
#             'snorkeling': hopiee.snorkeling,
#         })

#     # Return the serialized data as a JSON response
#     return JsonResponse({'hopiees': serialized_hopiees})


# #get data 
# from .models import Programs
# from django.http import JsonResponse

# def get_programs_data(request):
#     programs_data = Programs.objects.all().values()  # Retrieve all data from Programs table
#     return JsonResponse(list(programs_data), safe=False)





# from django.http import JsonResponse
# from .models import CustomUser

# def get_all_user_hobbies(request):
#     all_user_hobbies = CustomUser.objects.values_list('hobbies', flat=True)
#     return JsonResponse({"hobbies": list(all_user_hobbies)})

















# views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth import get_user_model
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from allauth.account.utils import send_email_confirmation

from .serializers import CustomUserSerializer

# views.py

from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
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

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        headers = self.get_success_headers(serializer.data)
        return Response({'detail': 'Please confirm your email address to complete the registration.',
                         'access_token': access_token},
                        status=status.HTTP_201_CREATED, headers=headers)


































#register


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from allauth.account.utils import send_email_confirmation


# # @csrf_exempt
# @api_view(['POST'])
# def register_user(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from django.db import transaction
# from django.core.mail import send_mail
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import UserSerializer
# from .models import CustomUser

# @api_view(['POST'])
# def register_user(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             send_confirmation_email(request, user)
#             return Response({'detail': 'Email confirmation sent. Please verify your email.'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def register_user_after_confirmation(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             confirmation_key = serializer.validated_data.get('confirmation_key')
#             user = complete_registration_after_confirmation(confirmation_key)
#             if user:
#                 refresh = RefreshToken.for_user(user)
#                 tokens = {
#                     'refresh': str(refresh),
#                     'access': str(refresh.access_token),
#                 }
#                 return Response({'detail': 'Registration successful.', 'tokens': tokens}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def send_confirmation_email(request, user):
#     confirmation_key = generate_confirmation_key()
#     user.confirmation_key = confirmation_key
#     user.save()

#     subject = 'Confirm your email'
#     message = f'Hi {user.username},\n\nPlease click the following link to confirm your email:\n\n{request.build_absolute_uri("/confirm/?key=" + confirmation_key)}'
#     from_email = 'your@example.com'  # Update with your email address
#     to_email = user.email

#     send_mail(subject, message, from_email, [to_email])

# def complete_registration_after_confirmation(confirmation_key):
#     try:
#         user = CustomUser.objects.get(confirmation_key=confirmation_key)
#         user.emailaddress_set.filter(email=user.email).update(verified=True)
#         return user
#     except CustomUser.DoesNotExist:
#         return None

# def generate_confirmation_key():
#     # Implement your logic to generate a unique confirmation key
#     import uuid
#     return str(uuid.uuid4())



# @api_view(['POST'])
# def register_user(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             send_email_confirmation(request, user)
            
#             # Optionally, you can generate a JWT token and include it in the response
#             refresh = RefreshToken.for_user(user)
#             tokens = {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }
            
#             return Response({'detail': 'Email confirmation sent. Please verify your email.'}, status=status.HTTP_201_CREATED)
#         # user = serializer.save()
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






    



#     # accounts/views.py/login

# from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from django.core.exceptions import ObjectDoesNotExist
# from rest_framework_simplejwt.tokens import RefreshToken

# # from .models import CustomUser

# @api_view(['POST'])
# def user_login(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         email = request.data.get('email')
#         password = request.data.get('password')

#         user = None

#         if email:
#             try:
#                 user = CustomUser.objects.get(email=email)
#             except ObjectDoesNotExist:
#                 pass
#         elif username:
#             user = authenticate(username=username, password=password)

#         if user and user.check_password(password):
#             refresh = RefreshToken.for_user(user)
#             access_token = refresh.access_token

#             print(f"Generated Refresh Token: {str(refresh)}")
#             print(f"Generated Access Token: {str(refresh.access_token)}")

#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(access_token),
#                 'token': token.key,
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
# views.py

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from allauth.account.models import EmailConfirmation
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # Check if the user has confirmed their email
        user = get_user_model().objects.get(username=request.data.get('username'))
        email_address = EmailAddress.objects.get(user=user, verified=True)

        if email_address:
            # User has confirmed their email, provide access and refresh tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            # token = Token.objects.create(user)
            
            # Add custom response data for successful login
            # Add custom response data for successful login
            # response.data['access_token'] = access_token
            # response.data['refresh_token'] = str(refresh)
            # response.data['token'] = access_token
            response.data['token_key'] = refresh.access_token.payload['jti']
            response.data['detail'] = 'Login successful.'


        return response

















# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import get_user_model
# from allauth.account.models import EmailAddress
# from rest_framework_jwt.views import ObtainJSONWebToken
# from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
# from rest_framework_jwt.settings import api_settings

# class CustomTokenObtainPairView(ObtainJSONWebToken):
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)

#         # Check if the user exists and has confirmed their email
#         username = request.data.get('username')
#         user = get_user_model().objects.get(username=username)
#         email_address = EmailAddress.objects.get(user=user, verified=True)

#         if email_address:
#             # User has confirmed their email, provide access and refresh tokens
#             payload = jwt_payload_handler(user)
#             token = jwt_encode_handler(payload)

#             # Add custom response data for successful login
#             response.data['token'] = token
#             response.data['detail'] = 'Login successful.'
#         else:
#             # User has not confirmed their email, invalidate the tokens
#             response.data = {}
#             response.status_code = status.HTTP_400_BAD_REQUEST
#             response.data['detail'] = 'Email not confirmed. Please confirm your email address.'

#         return response










# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from allauth.account.models import EmailAddress
# from rest_framework_simplejwt.tokens import RefreshToken

# class LogoutAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         try:
#             # Use the access token for authentication
#             user = request.user
#             email_address = EmailAddress.objects.get(user=user, verified=True)
#             refresh_token = request.headers.get('Authorization').split(' ')[1]
#             access_token_payload = RefreshToken(refresh_token).access_token.payload

#             if access_token_payload['jti'] == refresh_token :
#                 # Token and email are valid, blacklist the refresh token
#                 RefreshToken.for_user(user).blacklist()
#                 return Response({"detail": "Logout successful."}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"detail": "Invalid token or email not confirmed."},
#                                 status=status.HTTP_400_BAD_REQUEST)

#         except Exception as e:
#             return Response({"detail": "Invalid token or token not provided."},
#                             status=status.HTTP_400_BAD_REQUEST)






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
from .models import Programs
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
from .models import Programs
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
