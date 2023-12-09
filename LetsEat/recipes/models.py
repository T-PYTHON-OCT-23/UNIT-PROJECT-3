from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
        
    categories = models.TextChoices("Categories", ["brakfast",  "lunch", "dinner" ,"salad", "smoothie" , "sweet"])
    name  = models.CharField(max_length=2048)
    description = models.TextField()
    ingredients = models.TextField()
    preparing = models.TextField()
    published_at = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=64, choices=categories.choices)
    picture = models.ImageField(upload_to="img/" , default="img/default.png")


class Review(models.Model):
    recipe= models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    date= models.DateField(auto_now_add=True)
    review= models.TextField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to="img/" , default="img/default.png")

def __str__(self):
    return f"(self.name)"
