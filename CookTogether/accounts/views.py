from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError


def register_user(request: HttpRequest):
    msg = None
    if request.method=='POST':
        try:
            user=User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
            user.save()
            return redirect('main:home_page')
        except IntegrityError as e:
            msg = f"Please select another username"
        except Exception as e:
            msg = f"Unfortunately, we encountered an issue. Please try again later. {e}"
    return render(request,'accounts/register.html',{'msg':msg})

def login_page(request: HttpRequest):
    msg=None
    try:
        if request.method=='POST':
            user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
            if user:
                login(request,user)
                return redirect('main:home_page')
            else:
                msg='Please provide correct username or password'
    except Exception as e:
        msg = f"Unfortunately, we encountered an issue. Please try again later. {e}"
    return render(request,'accounts/login.html',{'msg':msg})

def logout_page(request: HttpRequest):
    try:
        if request.user.is_authenticated:
            logout(request)
        return redirect('accounts:login_page')
    except Exception:
        return redirect('accounts:login_page')

# Create your views here.
