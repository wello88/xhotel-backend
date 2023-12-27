from .views import RoomListCreateView, RoomDetailView, HotelListCreateView, get_program_by_id,ProgramsListCreateView,HotelDetailView,ProgramsDetailView
from django.urls import path

urlpatterns = [
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
    path('hotels/', HotelListCreateView.as_view(), name='hotel-list-create'),
    path('hotels/<str:pk>/', HotelDetailView.as_view(), name='hotel-detail'),
    path('programs/<int:program_id>/', get_program_by_id, name='get_program_by_id'),
    path('programs/', ProgramsListCreateView.as_view(), name='programs-list-create'),
    path('editprograms/<int:pk>/', ProgramsDetailView.as_view(), name='programs-detail'),

]
