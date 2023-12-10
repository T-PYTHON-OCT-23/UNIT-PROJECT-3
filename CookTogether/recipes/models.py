from django.db import models
from ingredients.models import Ingredient
from django.contrib.auth.models import User

class Recipe(models.Model):
    categories=models.TextChoices('categories',['Breakfast&Brunch','Lunch','Healthy','Appetizers&Snacks','Salad','SideDishes','Soups','Bread','Drinks','Desserts'])
    name=models.CharField(max_length=1000)
    description=models.TextField()
    kall=models.FloatField()
    time=models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient)
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
