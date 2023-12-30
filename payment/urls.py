# payments/urls.py
from django.urls import path
from .views import make_payment

urlpatterns = [
    path('make_payment/<int:booking_id>/', make_payment, name='make_payment'),
    # Add other URLs as needed
]
