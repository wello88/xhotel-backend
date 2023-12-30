from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from bookings.models import Hotel


from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
import string

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
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

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )

    def __str__(self):
        return self.username

class Registration(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    registration_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"Registration Code for {self.user.username}: {self.registration_code}"

@receiver(post_save, sender=CustomUser)
def create_registration(sender, instance, created, **kwargs):
    if created:
        Registration.objects.create(user=instance, registration_code=generate_registration_code())

def generate_registration_code():
    code_length = 6
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(code_length))