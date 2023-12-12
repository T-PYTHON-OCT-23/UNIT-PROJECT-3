from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    genders = models.TextChoices("genders" , ["female" , "male"])

    user = models.OneToOneField(User , on_delete=models.CASCADE)
    gender = models.CharField(max_length=7 , choices = genders.choices , default="female")
    birth_date = models.DateField(default='2023-01-01')


    def __str__(self) -> str:
        return self.user.first_name

