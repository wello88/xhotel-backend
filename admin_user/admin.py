from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Programs

@admin.register(Programs)
class ProgramsAdmin(admin.ModelAdmin):
    list_display = ('id', 'days', 'nights', 'massage', 'safari', 'camping', 'seatrip', 'diving', 'snorkeling')
 