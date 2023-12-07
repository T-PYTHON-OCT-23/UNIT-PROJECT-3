from django.db import models
from django.contrib.auth.models import User

class Services(models.Model):

    categories = models.TextChoices("Categories", ["Electrician and Plumber ", "Clining", "Water filling", "Moving furniture"])
    durations = models.TextChoices("Durations", ["Hours" , "Month"])

    name = models.CharField(max_length=2048)
    address = models.CharField(max_length=2048)
    image = models.ImageField(upload_to="image/" , default="image/default.jpg")
    about = models.TextField()
    nationality = models.CharField(max_length=2048)
    duration = models.CharField(max_length=2048, choices=categories.choices)
    quantity = models.IntegerField(null=True)
    city = models.CharField(max_length=2048)
    category = models.CharField(max_length=2048,choices=categories.choices )
    




