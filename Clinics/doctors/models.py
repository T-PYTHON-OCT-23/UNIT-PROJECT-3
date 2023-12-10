from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=256)
    avatar = models.ImageField(upload_to='image/', default='image/avatar.jpg')
    bio = models.TextField()


    def __str__(self) -> str:
        return self.name