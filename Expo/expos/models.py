from django.db import models
from django.contrib.auth.models import User

class News(models.Model):

    #choices
    categories = models.TextChoices("Categories", ["Event","Media"])
    
    title = models.CharField(max_length=2048)
    content = models.TextField()
    publishd_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=64, choices=categories.choices, default=categories.Event)
    poster = models.ImageField(upload_to="images/", default="images/default.jpg")

    def __str__(self):
        return f"{self.title}"

class Event(models.Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    poster = models.ImageField(upload_to="images/", default="images/events.png")
    date = models.DateTimeField()
    price = models.IntegerField()


class Reservation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"




# Create your models here.
