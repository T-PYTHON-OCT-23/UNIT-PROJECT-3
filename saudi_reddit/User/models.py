from django.db import models
from django.contrib.auth.models import User
from Fourm.models import Post, Comment, Subreddit

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', default=1)
    full_name = models.TextField(default='New_Redditor')
    email = models.EmailField(blank=True,unique=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/profiles/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    subreddit = models.ManyToManyField(Subreddit, blank=True)
    
    def __str__(self):
        return self.user.username