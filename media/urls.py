from django.urls import path
from .views import PictureList

urlpatterns = [
    path('api/pictures/', PictureList.as_view(), name='picture-list'),
]
