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

    def __str__(self):
        return f"{self.title}"


class Ticket(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    start_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.user.first_name} : {self.quantity}"



