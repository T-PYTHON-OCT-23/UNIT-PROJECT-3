from django.db import models

# Create your models here.


class Event(models.Model):

    categories = models.TextChoices("Categories", ["Art", "Healthcare", "Technology", "Entertainment"])

    title = models.CharField(max_length=2010)
    content = models.TextField()
    posting_date = models.DateField()
    category = models.CharField(max_length=100, choices=categories.choices)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")



