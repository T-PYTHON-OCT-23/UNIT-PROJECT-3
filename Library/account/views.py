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
         
            user = User.objects.create_user(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
            user.save()

            user_profile = Profile(user=user, avatar=request.FILES["avatar"], birth_date=request.POST["birth_date"])
            user_profile.save()

            return redirect("account:login_user_view")
        except IntegrityError as e:
            print(e)
            msg = f"Please select another username"
        except Exception as e:
            msg = f"something went wrong {e}"

    return render(request, "account/register.html", {"msg" : msg})


def login_user_view(request: HttpRequest):
    msg = None
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            login(request, user)
            return redirect("main:home_view")
        else:
            msg = "Please provide correct username and password"

    return render(request, "account/login.html", {"msg" : msg})


def logout_user(request: HttpRequest):

    if request.user.is_authenticated:
        logout(request)    

    return redirect("account:login_user_view")



def user_profile_view(request: HttpRequest, user_id):

    try:
        user = User.objects.get(id=user_id)
    except:
        return render(request, 'main/not_found.html')
    return render(request, 'account/profile.html', {"user":user})



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

                try:
                    profile : Profile = request.user.profile
                except Exception as e:
                    profile = Profile(user=user, birth_date=request.POST["birth_date"])
                    profile.save()

                profile.birth_date = request.POST["birth_date"]
                if 'avatar' in request.FILES: profile.avatar = request.FILES["avatar"]
                profile.about = request.POST["about"]
                profile.is_writer = request.POST["is_writer"]
                profile.instagram_link = request.POST["instagram_link"]
                profile.twitter_link = request.POST["twitter_link"]
                profile.save()

                return redirect("account:user_profile_view", user_id = request.user.id)

            else:
                return redirect("account:login_user_view")
        except IntegrityError as e:
            msg = f"Please select another username"
        except Exception as e:
            msg = f"something went wrong {e}"

    return render(request, "account/update.html", {"msg" : msg})