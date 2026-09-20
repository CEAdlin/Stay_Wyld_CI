# accounts/models.py

from django.db import models
from django.contrib.auth.models import User

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=120)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name
