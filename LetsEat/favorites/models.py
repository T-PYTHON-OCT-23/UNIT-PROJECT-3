from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

# Create your models here.


class Favorite(models.Model):

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):

        return f"{self.user.username} saved {self.recipe.name}."
    