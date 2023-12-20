from django.urls import path
from .views import EventBookingView
from . import views 
urlpatterns = [
    path('event/', EventBookingView.as_view(), name='book-event'),
    path('count-users-attending-event/', views.count_users_attending_event, name='count_users_attending_event'),

]
