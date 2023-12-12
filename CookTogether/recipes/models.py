from django.db import models
from ingredients.models import Ingredient
from django.contrib.auth.models import User

class Recipe(models.Model):
    categories=models.TextChoices('categories',['Breakfast&Brunch','Lunch','Appetizers','Salad','Soups','Bread','Drinks','Desserts'])
    name=models.CharField(max_length=1000)
    description=models.TextField()
    cal=models.FloatField()
    time=models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient)
    quantities_ingredients=models.TextField()
    instructions=models.TextField()
    image=models.ImageField(upload_to="images/")
    category=models.CharField(max_length=300,choices=categories.choices)


class Comment(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    rating=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    







# Create your models here.
