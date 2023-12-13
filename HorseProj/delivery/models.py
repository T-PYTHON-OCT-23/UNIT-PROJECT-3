from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Store(models.Model):
    name=models.CharField(max_length=256,default="")
    location=models.URLField(default="")
    work_time=models.CharField(max_length=256,default="")
    img=models.ImageField(upload_to="images/", default="images/default_store.jpg")
    rating=models.IntegerField(default=0)


class Menu(models.Model):
    menu_store=models.ForeignKey(Store,on_delete=models.CASCADE)
    name=models.CharField(max_length=256,default="")
    img=models.ImageField(upload_to="images/", default="images/default_menu.jpg")
    description=models.TextField(default="")
    price=models.IntegerField(default=0)

class MenuRequest(models.Model):
    menu=models.ForeignKey(Menu,on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    note=models.TextField(default="")

class StoreReview(models.Model):
    store_review=models.ForeignKey(Store, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating= models.IntegerField(default=0)
    comment=models.TextField(default="")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user}"