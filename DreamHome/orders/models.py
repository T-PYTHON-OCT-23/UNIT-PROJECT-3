from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
  
class Order(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.user.username   



class Repair(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
   
    your_city = models.TextChoices("your_city", ["Riyadh", "Jeddah", "Dammam", "Al-kharj"])
    
    full_name = models.CharField(max_length=2048)
    number= models.IntegerField()
    city = models.CharField(max_length=64, choices=your_city.choices, default="Cultural")
    address_details = models.TextField()
    total = models.IntegerField()


    def __str__(self):
        return f"{self.full_name} : {self.number}"