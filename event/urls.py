from django.urls import path
from .views import EventBookingView

urlpatterns = [
    path('event/', EventBookingView.as_view(), name='book-event'),
]
