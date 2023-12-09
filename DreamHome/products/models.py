from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
  
  choose_color = models.TextChoices("choose_color", ["White", "Black", "Beige", "Brown","Green","Blue"])
    
  name=models.CharField(max_length=2048) 
  content=models.TextField()
  size=models.IntegerField()
  choose_product= models.CharField(max_length=70, choices=choose_color.choices, default="Cultural" )
  product= models.ImageField(upload_to="images/", default="images/default.jpg")


  def __str__(self):
          return f"{self.name}"
  

class Review(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user} : {self.comment}"
  


  
    