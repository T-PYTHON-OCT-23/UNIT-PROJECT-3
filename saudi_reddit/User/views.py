
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login, authenticate , logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .emailNotfi  import send_mail
import os
from dotenv import load_dotenv
from .forms import SignUpForm
from django.contrib.auth.models import User as userauth
from User.models import Profile 
from User.forms import ProfileForm
from django.contrib.auth.decorators import login_required
from User.models import Post , Comment 
from subreddit.models import Subreddit

load_dotenv()

def signup(request):
    
    try:
        
        if request.method == 'POST':
            
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                print("user created")
                Profile.objects.create(user=user, email=user.email,full_name=user.full_name)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('/')
        #send_mail(subject='Welcome to Saudi Reddit',
        #message=f'Thank you for signing up to Saudi Reddit \n your username {user.username}', recipient_list=[user.email])
        else:
            form = SignUpForm()
    except Exception as e:

        print(e)
        messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, f'Welcome, {username}!')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('User:login')
        else:
            print(form.errors, form.error_messages)  
            return redirect('User:login')  
        
    else:   
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')

@login_required
def edit_profile(request):
    
    if not userauth.is_authenticated:
        return redirect('User:login')
    
    user = request.user
    profile = get_object_or_404(Profile, user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.instance.user = user
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('User:profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'registration/edit_profile.html', {'form': form, 'user_profile': profile})




def profile_Data(request,username):
    
    userauth1 = userauth.objects.get(username=username)
    user = Profile.objects.get(user=userauth1)
    
    posts = Post.objects.filter(author=userauth1)
    comments = Comment.objects.filter(author=userauth1)
    subreddits = Subreddit.objects.filter(subscribers=userauth1)
    author_subreddits = Subreddit.objects.filter(author=userauth1)
    
    user_profile = {
        
        'username': username,
        'email': user.email,
        'full_name': user.full_name,
        'bio': user.bio,
        'image': user.image.url if user.image else '',
        'created_at': user.created_at,
        'updated_at': user.updated_at,
        'post': posts,
        'comment': comments,
        'subreddit': subreddits,
        'author_subreddits': author_subreddits,
        'last_login': userauth1.last_login,
        
        
    }
    
    return render(request, 'registration/profile.html', {'user_profile': user_profile})


