# # # accounts/models.py

# # from django.contrib.auth.models import AbstractUser
# # from django.db import models

# # class CustomUser(AbstractUser):
# #     email = models.EmailField(unique=True)
# #     username = models.CharField(max_length=30,unique=True)
# #     first_name = models.CharField(max_length=255)
# #     last_name = models.CharField(max_length=255)
# #     country = models.CharField(max_length=255)
# #     zip = models.CharField(max_length=10)

# #     PROGRAM_CHOICES = [
# #         ('massage', 'Massage'),
# #         ('safari', 'Safari'),
# #         ('camping', 'Camping'),
# #         ('seatrip', 'Sea Trip'),
# #         ('diving', 'Diving'),
# #         ('snorkeling', 'Snorkeling'),
# #         # Add other programs as needed
# #     ]

# #     hobbies = models.CharField(max_length=255, choices=PROGRAM_CHOICES)  
# #     password = models.CharField(max_length=128) 

# #     def __str__(self):
# #         return self.username
    







# # #admin
# # from django.db import models

# # class Programs(models.Model):
# #     days = models.IntegerField(default=0)
# #     nights = models.IntegerField(default=0)  # Added field for nights
# #     massage = models.IntegerField(default=0)
# #     safari = models.IntegerField(default=0)
# #     camping = models.IntegerField(default=0)
# #     seatrip = models.IntegerField(default=0)
# #     diving = models.IntegerField(default=0)
# #     snorkeling = models.IntegerField(default=0)

# #     def save(self, *args, **kwargs):
# #         if not self.pk:  # This checks if the object is being created, not updated
# #             self.nights = self.days + 1
# #         super(Programs, self).save(*args, **kwargs)






































# # # models.py

# # from django.db import models
# # from django.conf import settings

# # class EmailConfirmation(models.Model):
# #     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# #     email = models.EmailField()
# #     confirmation_key = models.CharField(max_length=255)
# #     verified = models.BooleanField(default=False)

# #     def __str__(self):
# #         return f"{self.user.username}'s EmailConfirmation"

















# # accounts/models.py

# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     country = models.CharField(max_length=255)
#     zip = models.CharField(max_length=10)

#     PROGRAM_CHOICES = [
#         ('massage', 'Massage'),
#         ('safari', 'Safari'),
#         ('camping', 'Camping'),
#         ('seatrip', 'Sea Trip'),
#         ('diving', 'Diving'),
#         ('snorkeling', 'Snorkeling'),
#         # Add other programs as needed
#     ]

#     hobbies = models.CharField(max_length=255, choices=PROGRAM_CHOICES)  
#     password = models.CharField(max_length=128) 

#     def __str__(self):
#         return self.username
    







# #admin
# from django.db import models

# class Programs(models.Model):
#     days = models.IntegerField(default=0)
#     nights = models.IntegerField(default=0)  # Added field for nights
#     massage = models.IntegerField(default=0)
#     safari = models.IntegerField(default=0)
#     camping = models.IntegerField(default=0)
#     seatrip = models.IntegerField(default=0)
#     diving = models.IntegerField(default=0)
#     snorkeling = models.IntegerField(default=0)

#     def save(self, *args, **kwargs):
#         if not self.pk:  # This checks if the object is being created, not updated
#             self.nights = self.days + 1
#         super(Programs, self).save(*args, **kwargs)





















































































from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)

    PROGRAM_CHOICES = [
        ('massage', 'Massage'),
        ('safari', 'Safari'),
        ('camping', 'Camping'),
        ('seatrip', 'Sea Trip'),
        ('diving', 'Diving'),
        ('snorkeling', 'Snorkeling'),
    ]

    hobbies = models.CharField(max_length=255, choices=PROGRAM_CHOICES)
    password = models.CharField(max_length=128) 

    def str(self):
        return self.username







# #admin
# from django.db import models

# class Programs(models.Model):
#     days = models.IntegerField(default=0)
#     nights = models.IntegerField(default=0)  # Added field for nights
#     massage = models.IntegerField(default=0)
#     safari = models.IntegerField(default=0)
#     camping = models.IntegerField(default=0)
#     seatrip = models.IntegerField(default=0)
#     diving = models.IntegerField(default=0)
#     snorkeling = models.IntegerField(default=0)

#     def save(self, args, **kwargs):
#         if not self.pk:  # This checks if the object is being created, not updated
#             self.nights = self.days + 1
#         super(Programs, self).save(args, **kwargs)
    


    from django.db import models

class Programs(models.Model):
    days = models.IntegerField(default=0)
    nights = models.IntegerField(default=0)  # Added field for nights
    massage = models.IntegerField(default=0)
    safari = models.IntegerField(default=0)
    camping = models.IntegerField(default=0)
    seatrip = models.IntegerField(default=0)
    diving = models.IntegerField(default=0)
    snorkeling = models.IntegerField(default=0)

    def save(self, args, **kwargs):
        if not self.pk:  # This checks if the object is being created, not updated
            self.nights = self.days + 1
        super(Programs, self).save(args, **kwargs)

    class Meta:
        unique_together = ('id',)