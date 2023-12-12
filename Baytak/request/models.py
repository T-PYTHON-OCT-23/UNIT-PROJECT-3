from django.db import models
from django.contrib.auth.models import User
from services.models import Service

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    orderTime = models.DateTimeField()
    address = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    isDone = models.BooleanField(default = False)


    def __str__(self) -> str:
        return f"{self.user.first_name} : {self.service.name}"