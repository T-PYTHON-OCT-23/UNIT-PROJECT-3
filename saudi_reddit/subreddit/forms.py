from django import forms
from .models import Subreddit
from Fourm.models import Post, Comment
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author','title', 'content', 'subreddit' , 'image', 'video']  
        exclude = ['author', 'subreddit']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['video'].required = False

class SubredditForm(forms.ModelForm):
    class Meta:
        model = Subreddit
        fields = ['name', 'description', 'icon', 'author', 'slug','header']  
        exclude = ['author', 'slug']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        content = forms.CharField(widget=CKEditorWidget())
        fields = ['content', 'image', 'video', 'post', 'author']  
        exclude = ['author', 'post']
