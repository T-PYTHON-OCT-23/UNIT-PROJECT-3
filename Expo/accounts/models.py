from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    avatar = models.ImageField(upload_to="images/", default="images/avatar-default.png")


    def __str__(self):
        return f"{self.user.first_name} profile"

