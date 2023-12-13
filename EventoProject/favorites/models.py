from django.db import models
from django.contrib.auth.models import User
from events.models import Event

# Create your models here.


class Favorite(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return f"{self.user.username} favored {self.event.title}"