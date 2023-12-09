from django.db import models

# Create your models here.

class Store(models.Model):

    name=models.CharField(max_length=256,default="")
    location=models.URLField(default="")
    work_time=models.CharField(max_length=256,default="")
    img=models.ImageField(upload_to="images/", default="images/default_store.jpg")
    rating=models.IntegerField()


class Menu(models.Model):
    menu_store=models.ForeignKey(Store,on_delete=models.CASCADE)
    name=models.CharField(max_length=256,default="")
    img=models.ImageField(upload_to="images/", default="images/default_menu.jpg")
    description=models.TextField(default="")
    price=models.IntegerField(default="")