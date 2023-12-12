from django.db import models
from django.contrib.auth.models import User
from expos.models import *



# Create your models here.


class Bookmark(models.Model):

    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.user.username} bookmarked {self.news.title}"