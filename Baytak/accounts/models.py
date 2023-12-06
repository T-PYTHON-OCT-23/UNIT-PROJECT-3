from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="image/" , default="image/default.png")
    city = models.CharField(max_length=2048 , default="riyadh")
    mobileNumber = models.IntegerField()

    def __str__(self):
        return f"{self.user.first_name} profile"
