from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Service(models.Model):
    types = models.TextChoices('types',['Simple Storage','Server','RestFullAPI','Mobile SDK','Monitor Clint','Clint Endpoint', ])
    pricese = models.TextChoices('pricese',['1','2','3','4'])

    service_name = models.CharField(max_length=2028)
    description = models.TextField()
    type = models.CharField(max_length=1024,choices=types.choices)
    image = models.ImageField()
    price = models.CharField(max_length=1024,choices=pricese.choices)

    def __str__(self) -> str:
        return f"{self.service_name}"


class ServiceDetails(models.Model):
    publics = models.TextChoices('publics',['1.0.0.0','1.0.1.0','1.0.2.0','1.0.3.0','1.0.4.0','1.0.5.0','1.0.6.0','1.0.7.0','1.0.8.0','1.0.9.0','1.0.10.0','1.0.11.0','1.0.12.0','1.0.13.0','1.0.14.0','1.0.15.0','1.0.16.0'])
    pivates = models.TextChoices('privates',['2.0.0.0','2.0.1.0','2.0.2.0','2.0.3.0','2.0.4.0','2.0.5.0','2.0.6.0','2.0.7.0','2.0.8.0','2.0.9.0','2.0.10.0','2.0.11.0','2.0.12.0','2.0.13.0','2.0.14.0','2.0.15.0','2.0.16.0'])

    service = models.OneToOneField(Service,on_delete=models.CASCADE)
    private_endpoint = models.CharField(max_length=1024)
    public_endpoint = models.CharField(max_length=1024)
    private_ip = models.CharField(max_length=1024)
    public_ip = models.CharField(max_length=1024)
    elastic_ip = models.BooleanField(default=False)
    platfrom = models.CharField(max_length=2024)
    life_cycle = models.BooleanField(default=False)
    high_availability = models.BooleanField(default=False)