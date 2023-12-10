from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
  
class Order(models.Model):
    
    order = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.user.username   

#class Order(models.Model):

    #order_name = models.CharField(null=True, max_length=500)
    
    #def __str__(self):

       # return self.order_name

#class Client(models.Model):
      #name = models.CharField(null=True, max_length=20)
      #order =models.ForeignKey(Order, on_delete=models.CASCADE)          