from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
    
class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        # Set the user of the review to the currently logged-in user (if applicable)
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {'reviews': serializer.data}
        return Response(data, status=status.HTTP_200_OK) 

    # def get_queryset(self):
    #     return Review.objects.all()