from django.db import models
from datetime import date
from doctors.models import Doctor
from django.contrib.auth.models import User

# Create your models here.


class Clinic(models.Model):
    categories = models.TextChoices(
        "Categories", ["Gynecology", "Dentistry", "Pediatric", "Psychiatry", "Neurology", "Dermatology"])

    name = models.CharField(max_length=512)
    about = models.TextField()
    category = models.CharField(
        max_length=2048, choices=categories.choices, default="Coffee")
    image = models.ImageField(upload_to="image/", default="image/default.jpg")
    location = models.URLField()
    doctors = models.ManyToManyField(Doctor)


class Review(models.Model):
    Clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    user_name = models.CharField(max_length=210)
    email = models.EmailField()
    message = models.TextField()
