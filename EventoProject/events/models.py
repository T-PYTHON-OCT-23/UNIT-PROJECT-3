from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Event(models.Model):

    categories = models.TextChoices("Categories", ["Art", "Technology", "Entertainment","Exclusive"])

    title = models.CharField(max_length=2010)
    content = models.TextField()
    posting_date = models.DateField()
    category = models.CharField(max_length=100, choices=categories.choices)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")



class Review(models.Model):
    ratings = models.TextChoices("Ratings", ["Excellent","Good", "Average", "Poor", "Very poor"])

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.CharField(max_length=80,choices=ratings.choices)
    posting_date = models.DateTimeField(auto_now_add=True)


