from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
    
# class ReviewList(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def perform_create(self, serializer):
#         # Set the user of the review to the currently logged-in user (if applicable)
#         serializer.save(user=self.request.user)

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         data = {'reviews': serializer.data}
#         return Response(data, status=status.HTTP_200_OK) 

#     # def get_queryset(self):
#     #     return Review.objects.all()




#     from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json

# @csrf_exempt  # For simplicity; use a proper CSRF protection mechanism in production
# def register_user(request):
#     if request.method == 'POST':
#         try:
#             # Parse the JSON data from the request body
#             data = json.loads(request.body.decode('utf-8'))

#             # Get the username and password from the JSON data
#             username = data.get('username')
#             password = data.get('password')

#             # Your registration logic here
#             # For example, you can create a new user using Django's User model
#             # user = User.objects.create(username=username, password=password)

#             return JsonResponse({'message': 'User registered successfully'})
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON data'}, status=400)
#     else:
#         return JsonResponse({'error': 'Unsupported method'}, status=405)
    

    
from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
import json

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        # Set the user of the review to the currently logged-in user (if applicable)
        serializer.save(user=self.request.user)

    def list(self, request, args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {'reviews': serializer.data}
        return Response(data, status=status.HTTP_200_OK) 

    def create(self, request,args, **kwargs):
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body.decode('utf-8'))

            # Get the username and password from the JSON data
            username = data.get('username')
            password = data.get('password')

            # Create a new user
            user = User.objects.create_user(username=username, password=password)

            # You may want to perform additional actions here, like logging the user in.

            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)