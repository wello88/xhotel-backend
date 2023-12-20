# admin.py

from django.contrib import admin
#admin
from django.contrib import admin
from .models import Programs,CustomUser

@admin.register(Programs)
class ProgramsAdmin(admin.ModelAdmin):
    list_display = ('id', 'days', 'nights', 'massage', 'safari', 'camping', 'seatrip', 'diving', 'snorkeling')
    # Add more fields to the list_display if needed

# from django.contrib import admin
# from .models import CustomUser
# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name', 'country', 'zip', 'hobbies')
#     search_fields = ('username', 'email')

#     actions = ['create_user_from_admin']

#     def create_user_from_admin(self, request, queryset):
#         for user in queryset:
#             # You may customize the data you want to use for creating users here
#             # For simplicity, this example uses default values for some fields
#             CustomUser.objects.create(
#                 username=user.username,
#                 email=user.email,
#                 password='',  # Provide a default or let the user set it later
#                 first_name=user.first_name,
#                 last_name=user.last_name,
#                 country=user.country,
#                 zip=user.zip,
#                 hobbies=user.hobbies
#             )
#         self.message_user(request, f'Successfully created {queryset.count()} users.')

#     create_user_from_admin.short_description = 'Create users from selected CustomUser instances'

# admin.site.register(CustomUser, CustomUserAdmin)
