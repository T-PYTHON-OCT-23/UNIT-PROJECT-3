from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class consultation(models.Model):
    categories=models.TextChoices("categories",["Horse health", "Horse riding","Buying horses"," horse training","General consultations"])

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title=models.CharField(max_length=256)
    category=models.CharField(max_length=256,choices=categories.choices, default="")
    description=models.TextField(default="")
    age_horse=models.IntegerField()
    horse_type=models.CharField(max_length=256)
   


    

