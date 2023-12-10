from django.db import models
from recipes.models import Recipe
from django.contrib.auth.models import User
class Favorite(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
# Create your models here.
