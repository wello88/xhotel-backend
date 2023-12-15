# admin.py

from django.contrib import admin
#admin
from django.contrib import admin
from .models import Programs

@admin.register(Programs)
class ProgramsAdmin(admin.ModelAdmin):
    list_display = ('id', 'days', 'nights', 'massage', 'safari', 'camping', 'seatrip', 'diving', 'snorkeling')
    # Add more fields to the list_display if needed
