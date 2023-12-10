from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register_user(request: HttpRequest):
    if request.method=='POST':
        user=User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
        user.save()
        return redirect('accounts:login_page')
    return render(request,'accounts/register.html')

def login_page(request: HttpRequest):
    msg=None
    if request.method=='POST':
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user:
            login(request,user)
            return redirect('main:home_page')
        else:
            msg='Please provide correct username or password'
    return render(request,'accounts/login.html',{'msg':msg})

def logout_page(request: HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    return redirect('accounts:login_page')

# Create your views here.
