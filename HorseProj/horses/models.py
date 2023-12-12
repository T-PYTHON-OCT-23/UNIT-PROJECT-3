from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class StableHorses(models.Model):
    name=models.CharField(max_length=256, default="")
    img=models.ImageField(upload_to="images/", default="images/default.jpg")
    city=models.CharField(max_length=256 , default="")
    description=models.TextField(default="")
    rating = models.IntegerField(default=0)



class ServicesStable(models.Model):
    stbleHorse=models.ForeignKey(StableHorses,on_delete=models.CASCADE)
    name_Servic=models.CharField(max_length=256,default="")
    description_Servic=models.TextField(default="")
    duration_service=models.CharField(max_length=256,default="")
    price=models.IntegerField(default=0)


class StableRequest(models.Model):
    services=models.ForeignKey(ServicesStable,on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    note=models.TextField(default="")




class Reviews(models.Model):
    horses=models.ForeignKey(StableHorses, on_delete=models.CASCADE)


    user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating= models.IntegerField(default=0)
    comment=models.TextField(default="")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user}"
