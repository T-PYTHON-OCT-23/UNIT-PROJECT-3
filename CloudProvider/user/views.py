from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.


def user_create_view(request:HttpRequest):
    msg = ''
    if request.method == 'POST':

        try:
            new_user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
            new_user.save()
            return redirect('user:login_view')
        except Exception as e:
            msg = f'something went wrong, {e}'
    

    return render(request,'user/registraction.html',{'msg':msg})


def login_view(request:HttpRequest):
    msg = ''
    
    if request.method == 'POST':

        try:
            user = authenticate(request,username= request.POST['username'],password=request.POST['password'])

            if user:
                login(request,user)
                return redirect('home:home_view')
            else:
                msg = 'email or password is not valid'
        except Exception as e:
            msg = f'something went wrong, {e}'

    return render(request,'user/login.html',{'msg':msg})


def logout_view(request:HttpRequest):
    
    if request.user.is_authenticated:
        logout(request)
        return redirect('user:login_view')