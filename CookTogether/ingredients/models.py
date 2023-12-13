from django.db import models
class Ingredient(models.Model):
    name=models.CharField(max_length=1000)
    description=models.TextField()
    image=models.ImageField(upload_to="images/")   

# Create your models here.
