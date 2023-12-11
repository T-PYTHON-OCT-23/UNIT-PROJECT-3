from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import Profile

# Create your views here.


def register_user_view(request: HttpRequest):
    msg = None

    if request.method == "POST":
        try:
            #create a new user
            user = User.objects.create_user(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
            user.save()

            user_profile = Profile(user=user, avatar=request.FILES["avatar"], birth_date=request.POST["birth_date"])
            user_profile.save()
            return redirect("accounts:success_page_view")

        except IntegrityError as e:
            msg = f"Please select another username"
        except Exception as e:
            msg = f"something went wrong {e}"
        

    return render(request, "accounts/register.html", {"msg" : msg})

def success_page_view(request:HttpRequest):
    return render(request, "accounts/success_page.html")

def login_user_view(request:HttpRequest):
    msg = None
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        
        if user:
            login(request, user)
            return redirect("main:home_page_view")
        else:
            msg = "Please provide correct username and password"

    return render(request, "accounts/login_page.html", {"msg" : msg})



def logout_user_view(request:HttpRequest):
    
    if request.user.is_authenticated:
        logout(request)    

    return redirect("accounts:login_user_view")


def user_profile_view(request: HttpRequest, user_id):
        
    user = User.objects.get(id=user_id)

    return render(request, 'accounts/profile_page.html', {"user":user})
