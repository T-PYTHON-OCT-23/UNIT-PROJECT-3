from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cities = models.Choices("cities",["Riyadh","Jeddah","Damamm"])
    
    phone_number=models.CharField(max_length=64)
    city = models.CharField(max_length=64,choices=cities.choices)
    
