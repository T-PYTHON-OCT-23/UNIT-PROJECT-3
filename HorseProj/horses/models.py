from django.db import models


# Create your models here.
class StableHorses(models.Model):
    name=models.CharField(max_length=256, default="")
    img=models.ImageField(upload_to="images/", default="images/default.jpg")
    city=models.CharField(max_length=256 , default="")
    description=models.TextField(default="")
    rating = models.IntegerField(default="")



class ServicesStable(models.Model):
    stbleHorse=models.ForeignKey(StableHorses,on_delete=models.CASCADE)
    name_Servic=models.CharField(max_length=256,default="")
    description_Servic=models.TextField(default="")
    duration_service=models.CharField(max_length=256,default="")
    price=models.IntegerField(default="")


