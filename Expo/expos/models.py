from django.db import models
from django.contrib.auth.models import User

class News(models.Model):

    #choices
    categories = models.TextChoices("Categories", ["Event","Media"])

    title = models.CharField(max_length=2048)
    content = models.TextField()
    publishd_at = models.DateTimeField()
    category = models.CharField(max_length=64, choices=categories.choices, default=categories.Event)
    poster = models.ImageField(upload_to="images/", default="images/default.jpg")

    def __str__(self):
        return f"{self.title}"
    

# Create your models here.
