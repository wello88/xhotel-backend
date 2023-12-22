# profile/urls.py
from django.urls import path
from .views import UserProfileAPIView,UserProfileView

urlpatterns = [
    path('profile/', UserProfileAPIView.as_view(), name='profile-detail'),
    path('pprofile/',UserProfileView.as_view(),name='bookingdata')
]
