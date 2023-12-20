
# bookings/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Hotel, Room, HotelBooking

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(HotelBooking)


# Register your models here.
from accounts.models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','hobbies')

admin.site.register(CustomUser)