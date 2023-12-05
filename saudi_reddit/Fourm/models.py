# myredditapp/models.py

from django.db import models
from django.contrib.auth.models import User

class Subreddit(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/headers/', blank=True)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    Subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images/posts/', blank=True)
    video = models.FileField(upload_to='videos/posts/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='images/comments/', blank=True)
    video = models.FileField(upload_to='videos/comments/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.content

