from django.db import models
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.
class Favorite(models.Model):
    
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.user.username} favored {self.book.name}"

