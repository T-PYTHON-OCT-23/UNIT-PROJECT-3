from django.db import models
from django.contrib.auth.models import User


class Art(models.Model):
    title=models.CharField(max_length=100)
    poster = models.ImageField(upload_to="images/")
   
   
    def __str__(self):
        return f"{self.title}"
    

class Review(models.Model):
    art = models.ForeignKey(Art,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} : {self.comment}"
