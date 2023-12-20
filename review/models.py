from django.db import models

# Create your models here.
from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=20)
    # hotel = models.CharField(max_length=100)
    comment = models.TextField()