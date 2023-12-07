# User/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as userauth
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    full_name = forms.CharField(max_length=255, help_text='Required. Enter your full name.')

    class Meta:
        model = userauth
        fields = ('username', 'email','full_name', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('full_name','email', 'bio','image')