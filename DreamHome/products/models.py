from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
  
  choose_color = models.TextChoices("choose_color", ["White", "Black", "Beige", "Brown","Green","Blue"])
    
  name=models.CharField(max_length=2048) 
  content=models.TextField()
  size=models.IntegerField()
  choose_co = models.CharField(max_length=70, choices=choose_color.choices, default="Cultural" )
  product= models.ImageField(upload_to="images/", default="images/default.jpg")


  def __str__(self):
          return f"{self.name}"
  
    