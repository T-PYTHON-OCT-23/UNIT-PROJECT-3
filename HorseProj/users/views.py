from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import Profile
# Create your views here.


def register_views(request:HttpRequest):
    msg=None
    if request.method == "POST":
        try:
            if User.objects.filter(email=request.POST["email"]).exists():
                raise Exception("Email address must be unique. Please choose another email.")
            user= User.objects.create_user(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
            user.save()

            profile = Profile(user=user)
            profile.save()

            
            return redirect("users:login_views")
        
        except IntegrityError as e:
            msg = "Username must be unique. Please choose another username."

        except Exception as e:
            msg = f"Something went wrong. Please try again. {e}"

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


def user_profile_view(request: HttpRequest, user_id):

    try:
        
        user = User.objects.get(id=user_id)

    except Exception as e :
        print(e)

    return render(request, 'users/profile.html', {"user":user})


def update_user_view(request: HttpRequest):
    msg = None

    if request.method == "POST":
        try:
            if request.user.is_authenticated:
                user : User = request.user
                user.first_name = request.POST["first_name"]
                user.last_name = request.POST["last_name"]
                user.email = request.POST["email"]
                user.save()

               
                profile : Profile = request.user.profile

                profile.birth_date = request.POST["birth_date"]
                if 'avatar' in request.FILES: profile.avatar = request.FILES["avatar"]
                profile.about = request.POST["about"]
                profile.have_horse= request.POST["have_horse"]
                profile.level = request.POST["level"]
                profile.save()

                return redirect("users:user_profile_view", user_id = request.user.id)

            else:
                return redirect("users:login_views")
        except IntegrityError as e:
            msg = f"Username must be unique. Please choose another username."
       

    return render(request, "users/update_profile.html", {"msg" : msg})