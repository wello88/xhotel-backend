from django.db import models

# Create your models here.
from django.db import models

class Review(models.Model):
    user = models.CharField(max_length=100)
    # hotel = models.CharField(max_length=100)
    comment = models.TextField()