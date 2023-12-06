from django import forms
from .models import Subreddit
from Fourm.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author','title', 'content', 'subreddit' , 'image', 'video']  

class SubredditForm(forms.ModelForm):
    class Meta:
        model = Subreddit
        fields = ['name', 'description', 'icon', 'author', 'slug','header']  

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'image', 'video', 'post', 'author']  
