from django.db import models
# Create your models here.

class Event(models.Model):

    #choices
    categories = models.TextChoices("Categories", ["Technology", "Art", "Fashion", "Healthcare"])

    title = models.CharField(max_length=2040)
    description = models.TextField()
    release_date = models.DateField()
    category = models.CharField(max_length=80, choices=categories.choices, default=categories.Art)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")



    
