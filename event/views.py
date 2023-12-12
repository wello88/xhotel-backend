from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer

class EventBookingView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request, *args, **kwargs):
        check_in_dates = Event.objects.values_list('check_in', flat=True)
        return Response(list(check_in_dates))
