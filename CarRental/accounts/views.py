from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError


# Create your views here.

def register_user_view(request: HttpRequest):
    msg = None
    if request.method == "POST":
        try:
            #create a new user
            user = User.objects.create_user(
            username = request.POST["username"],
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            password1=request.POST["password1"],
            password2=request.POST["password2"],
            )
            return redirect("accounts:login_user_view")
        except IntegrityError as e:
            msg = f"Please select another username"
        except Exception as e:
            msg = f"something went wrong {e}"

    return render(request, "accounts/register.html", {"msg" : msg})
   

def login_user_view(request: HttpRequest):
    msg = None
    if request.method == "POST":
        #firt : authenticate the user data
        user = authenticate(request, 
                            username=request.POST["username"],
                            password=request.POST["password"]
                            )
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