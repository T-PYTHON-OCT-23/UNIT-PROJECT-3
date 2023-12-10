from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Service(models.Model):
    types = models.TextChoices('types',['storage','server'])

    service_name = models.CharField(max_length=2028)
    description = models.TextField()
    type = models.CharField(max_length=1024,choices=types.choices)
    image = models.ImageField()
    price = models.CharField(max_length=1024)

    def __str__(self) -> str:
        return f"{self.service_name}"