from django.urls import path
from .views import ReviewList
from . import views
urlpatterns = [
    path('api/reviews/', ReviewList.as_view(), name='review-list'),
    path('count-users-with-reviews/',views.count_users_with_reviews, name='count_users_with_reviews'),

]