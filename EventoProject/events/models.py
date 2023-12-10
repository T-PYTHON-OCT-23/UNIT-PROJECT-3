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



class Ticket(models.Model):
    quantity = models.TextChoices("Quantity", ["1","2", "3", "4", "5"])

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=80,choices=quantity.choices)
    start_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField(auto_now_add=True)



