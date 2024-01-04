# payments/urls.py
from django.urls import path
from .views import index

urlpatterns = [
    path('payment/', index, name='make_payment'),
    # Add other URLs as needed
]
