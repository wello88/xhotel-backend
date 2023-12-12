from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer

    
class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        # Set the user of the review to the currently logged-in user (if applicable)
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Customize the queryset based on your requirements (optional)
        return Review.objects.all()