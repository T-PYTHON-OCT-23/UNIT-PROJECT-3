from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    birth_date = models.DateField()
    avatar = models.ImageField(upload_to="images/", default="images/avatar.jpg")
    twitter_link = models.URLField()
    instagram_link = models.URLField()

    def __str__(self):
        return f"{self.user.first_name} profile"


