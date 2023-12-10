from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import Profile, Appointment
from main.models import Clinic
# Create your views here.


def register(request: HttpRequest):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST["username"], first_name=request.POST["first_name"],
                                        last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
        user.save()
        return redirect("client:login_user")

    return render(request, "client/register.html")


def login_user(request: HttpRequest):
    msg = None
    if request.method == "POST":
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])

        if user:
            login(request, user)
            return redirect("main:home_view")
        else:
            msg = "Please provide correct username and password"
    return render(request, "client/login.html", {"msg": msg})


def logout_user(request: HttpRequest):

    if request.user.is_authenticated:
        logout(request)

    return redirect("client:login_user")


def user_profile(request: HttpRequest, user_id):

    try:
        user = User.objects.get(id=user_id)

    except:
        return render(request, 'main/not_found.html')

    return render(request, 'client/profile.html', {"user": user})


def update_user(request: HttpRequest):
    msg = None

    if request.method == "POST":
        try:
            if request.user.is_authenticated:
                user: User = request.user
                user.first_name = request.POST["first_name"]
                user.last_name = request.POST["last_name"]
                user.email = request.POST["email"]
                user.save()

                try:
                    profile: Profile = request.user.profile
                except Exception as e:
                    profile = Profile(
                        user=user, birth_date=request.POST["birth_date"])
                    profile.save()

                profile.birth_date = request.POST["birth_date"]
                if 'avatar' in request.FILES:
                    profile.avatar = request.FILES["avatar"]
                profile.about = request.POST["about"]
                profile.instagram_link = request.POST["instagram_link"]
                profile.twitter_link = request.POST["twitter_link"]
                profile.save()

                return redirect("client:user_profile", user_id=request.user.id)

            else:
                return redirect("client:login_user")
        except IntegrityError as e:
            msg = f"Please select another username"
        except Exception as e:
            msg = f"something went wrong {e}"

    return render(request, "client/update.html", {"msg": msg})


def appoinment(request: HttpRequest, clinic_id): 
    if not request.user.is_authenticated:
        return redirect("client:login_user")

    try:
        clinic = Clinic.objects.get(id=clinic_id)
        
        new_appointment = Appointment(user=request.user, clinic=clinic)
        new_appointment.save()

        return redirect("main:clinic_detail", clinic_id=clinic.id)
    except Exception as e:
        return redirect("main:home_view")
    
def my_appoinment(request: HttpRequest):

    appoinment = Appointment.objects.filter(user=request.user)
    return render(request, 'client/appoinment.html', {"appoinment" : appoinment})
    

