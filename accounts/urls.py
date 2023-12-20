# accounts/urls.py

# from django.urls import path
# from .views import register_user, user_login, user_logout,change_password,get_all_user_hobbies

# urlpatterns = [
#     path('register/', register_user, name='register'),
#     path('login/', user_login, name='login'),
#     path('logout/', user_logout, name='logout'),
#     path('change_password/', change_password, name='change_password'),
#     path('gethobbies/', get_all_user_hobbies ,name='hobbies'),
# ]






from django.urls import path
from .views import RegistrationAPIView,LogoutAPIView,change_password,get_all_user_hobbies,CustomTokenObtainPairView
from . import views  # Import the views module from your app
from allauth.account.views import ConfirmEmailView
from allauth.account.views import LoginView
from .views import get_email_by_user_id


urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/',CustomTokenObtainPairView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('change_password/', change_password, name='change_password'),
    path('gethobbies/', get_all_user_hobbies ,name='hobbies'),
    path('count-Registerd-users/',views.count_custom_users, name='count_custom_users'),
    path('accounts/confirm-email/<str:key>/', ConfirmEmailView.as_view(), name='account_confirm_email'),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path('user-email/', get_email_by_user_id, name='user-email'),


]