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
    privates = models.TextChoices('privates',['2.0.0.0','2.0.1.0','2.0.2.0','2.0.3.0','2.0.4.0','2.0.5.0','2.0.6.0','2.0.7.0','2.0.8.0','2.0.9.0','2.0.10.0','2.0.11.0','2.0.12.0','2.0.13.0','2.0.14.0','2.0.15.0','2.0.16.0'])
    privates_endpoint = models.TextChoices('privates_endpoint',['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22'])
    publics_endpoint = models.TextChoices('publics_endpoint',['300','400','500','600','700','800','900','1000','1100','1200','1300','1400','1500','1600','1700','1800','1900','2000','2100','2200'])
    platforms = models.TextChoices('platforms',['Linux','Ububtu','Windows','Unix','CloudLinux'])
    elastic_ips = models.TextChoices('elastic_ips',['True','False'])
    life_cycles = models.TextChoices('life_cycles',['True','False'])
    high_availabilitys = models.TextChoices('high_availabilitys',['True','False'])

    service = models.OneToOneField(Service,on_delete=models.CASCADE)
    private_endpoint = models.CharField(max_length=1024,choices=privates_endpoint.choices)
    public_endpoint = models.CharField(max_length=1024,choices=publics_endpoint.choices)
    private_ip = models.CharField(max_length=1024,choices=privates.choices)
    public_ip = models.CharField(max_length=1024,choices=publics.choices)
    elastic_ip = models.BooleanField(default=False,choices=elastic_ips.choices)
    platfrom = models.CharField(max_length=2024,choices=platforms.choices)
    life_cycle = models.BooleanField(default=False,choices=life_cycles.choices)
    high_availability = models.BooleanField(default=False,choices=high_availabilitys.choices)

    def __str__(self) -> str:
        return f'{self.service}'


class ServiceRequest(models.Model):

    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.user} request {self.service}'