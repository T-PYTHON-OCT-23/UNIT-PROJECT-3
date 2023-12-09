from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
# Create your views here.


def register_views(request:HttpRequest):
    msg=None
    if request.method == "POST":
        try:
            user= User.objects.create_user(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
            user.save()
            return redirect("users:login_views")
        
        except IntegrityError as e:
            # Handle IntegrityError for email uniqueness
            if 'unique constraint' in str(e).lower() and 'email' in str(e).lower():
                msg = "Email address must be unique. Please choose another email."
            else:
                msg = "Username must be unique. Please choose another username."

        except Exception as e:
            # Handle other exceptions
            msg = "Something went wrong. Please try again."

    return render(request,"users/register.html",{"msg":msg})

def login_views(request:HttpRequest):

    msg=None

    if request.method=="POST":
        user= authenticate(request,username=request.POST["username"],password=request.POST["password"])

        if user :
            login(request , user)
            return redirect("main:home_view")
        else:
            msg="Please enter correct username and password"


    return render (request, "users/login.html", {"masg":msg})

def logout_views(request:HttpRequest):

    if request.user.is_authenticated:
        logout(request)    

    return redirect("users:login_views")


def update_profile_view(request: HttpRequest, user_id):

    
    return render (request, "users/update_profile.html")


def user_profile_view(request: HttpRequest, user_id):

    try:
        
        user = User.objects.get(id=user_id)

    except Exception as e :
        print(e)
       
    

    return render(request, 'usres/profile.html', {"user":user})