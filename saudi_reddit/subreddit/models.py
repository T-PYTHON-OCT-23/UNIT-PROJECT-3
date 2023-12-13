from django.db import models

from django.contrib.auth.models import User
from django.utils.text import slugify




class Subreddit(models.Model):
    name = models.CharField(max_length=255,default='New Subreddit')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,default=1)
    subscribers = models.ManyToManyField(User, related_name='subscribers', blank=True, default=None)
    views = models.IntegerField(default=0)
    header = models.ImageField(upload_to='images/headers/', blank=True)
    icon = models.ImageField(upload_to='images/icons/', blank=True)
    slug = models.SlugField(max_length=255,unique=True)
    description = models.TextField(default='New Subreddit')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name) 
            self.slug = base_slug
            count = 1
            while self.__class__.objects.filter(slug=self.slug).exists(): 
                self.slug = f"{base_slug}-{count}"
                count += 1
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name