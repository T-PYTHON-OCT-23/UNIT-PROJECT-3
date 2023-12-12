


from django.db import models
from django.contrib.auth.models import User
from Art.models import Art

# Create your models here.


class Favorite(models.Model):

    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.user.username} favored {self.art.title}"