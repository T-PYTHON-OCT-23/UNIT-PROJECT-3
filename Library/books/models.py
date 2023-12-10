from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):

    categories = models.TextChoices("Categories", ["literature", "philosophy", "novel", "psychic", "sciences"])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    brief = models.TextField()
    writer = models.CharField(max_length=200)
    release_date = models.DateField()
    publishing_house = models.CharField(max_length=200)
    category = models.CharField(max_length=64, choices=categories.choices, default=categories.choices)
    poster = models.ImageField(upload_to="images/",default="images/default.jpg")
    content= models.FileField(upload_to="pdf/",default="pdf/default.pdf")


    def __str__(self):
        return f"{self.name}"
    

class Review(models.Model):
    book =  models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user} : {self.comment}"


