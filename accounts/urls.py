# accounts/urls.py

from django.urls import path
from .views import register_user, user_login, user_logout,change_password,get_all_user_hobbies

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('change_password/', change_password, name='change_password'),
    path('gethobbies/', get_all_user_hobbies ,name='hobbies'),
]