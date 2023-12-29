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
    from django.contrib.auth.models import AbstractUser,Group,Permission
    from django.utils.translation import gettext as _


    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )
    def str(self):
        return self.username
    
    