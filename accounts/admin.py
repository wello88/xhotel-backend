# admin.py

from django.contrib import admin
from .models import Hotel, Room

admin.site.register(Hotel)
admin.site.register(Room)

from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)