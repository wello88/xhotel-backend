# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    hobbies = models.CharField(max_length=255)
    password = models.CharField(max_length=128) 

    def __str__(self):
        return self.username
    







#admin
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

    def save(self, *args, **kwargs):
        if not self.pk:  # This checks if the object is being created, not updated
            self.nights = self.days + 1
        super(Programs, self).save(*args, **kwargs)






