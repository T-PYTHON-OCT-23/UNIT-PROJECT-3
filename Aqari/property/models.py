from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile

# Create your models here.
class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rental_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    floor = models.PositiveIntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='images/',default='images/default.jpg')

    def _str_(self):
        return self.title

class Rental(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rent_from = models.DateField(default="2020-01-01")
    rent_to = models.DateField(default="2020-01-01")
    tenant=models.ForeignKey(User,on_delete=models.CASCADE)

    def _str_(self):
        return f"Rental for {self.property.title}"

class Sale(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")
    buyer=models.ForeignKey(User,on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Sale of {self.property.title}"
class Comment(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField()
    rating = models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.user.username} on {self.property.title}'
