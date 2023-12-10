from django.db import models
from datetime import date

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


class Review(models.Model):
    Clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=512)
    rating = models.FloatField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    user_name = models.CharField(max_length=210)
    email = models.EmailField()
    message = models.TextField()
