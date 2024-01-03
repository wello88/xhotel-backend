from django.db import models

# ------------------------Programs for the Customer------------------------------- 
from django.db import models

class Programs(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    days = models.IntegerField(default=0)
    nights = models.IntegerField(default=0)
    massage = models.IntegerField(default=0)
    safari = models.IntegerField(default=0)
    camping = models.IntegerField(default=0)
    seatrip = models.IntegerField(default=0)
    diving = models.IntegerField(default=0)
    snorkeling = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.nights = self.days + 1
        super().save(*args, **kwargs)  # Call the superclass's save method 

# ------------------------ Programs for the Customer-------------------------------
        







from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUserr(AbstractUser):
    email = models.EmailField(unique=True)
    is_email_confirmed = models.BooleanField(default=False)