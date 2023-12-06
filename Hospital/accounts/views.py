from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def register_user_view(request: HttpRequest):

    if request.method == "POST":
        #create a new user
        user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"])
        user.save()
        return redirect("accounts:login_user_view")

    return render(request, "accounts/register.html")


def login_user_view(request: HttpRequest):
    msg = None
    if request.method == "POST":
        #firt : authenticate the user data
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            #second: login the user
            login(request, user)
            return redirect("main:home_view")
        else:
            msg = "Please provide correct username and password"



    return render(request, "accounts/login.html", {"msg" : msg})



def logout_user_view(request: HttpRequest):

    #log out the user
    if request.user.is_authenticated:
        logout(request)    

    return redirect("accounts:login_user_view")