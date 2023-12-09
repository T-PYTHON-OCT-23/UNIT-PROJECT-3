from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    about=models.TextField(default="")
    have_horse=models.BooleanField(default=True)
    level=models.BooleanField(default=True)
    birth_date = models.DateField()
    avatar = models.ImageField(upload_to="images/", default="images/avatar_default.jpg")


    def __str__(self) -> str:
        return f"{self.user.first_name} profile"

