from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Objective(models.Model):
    categories = models.TextChoices("Categories",["Equipment", "Houseware", "Agriculture tools", "Car tools","Other"])
    
    name = models.CharField(max_length=2048)
    description = models.TextField()
    category = models.CharField(max_length=64, choices=categories.choices, default=categories.Other)
    poster = models.ImageField(upload_to="imgs/", default="imgs/default.jpg")
    reserved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    


