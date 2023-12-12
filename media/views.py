from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Picture
from .serializers import PictureSerializer

class PictureList(generics.ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer