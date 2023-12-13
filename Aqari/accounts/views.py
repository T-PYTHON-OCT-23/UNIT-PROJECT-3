from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import UserProfile
from property.models import Property , Rental ,Sale
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings


# Create your views here.
def register_user_view(request: HttpRequest):
    
    msg=None
    if request.user.is_authenticated:
        return render(request, 'accounts/profile.html')
    elif request.method == "POST":
        try:
            
            user = User.objects.create_user(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
            user.save()

            user_profile = UserProfile(user=user, profile_picture = request.FILES["profile_picture"])
            user_profile.save()
            login(request,user)
            subject = 'welcome to Aqari world'.upper()
            message = f'Hi {user.first_name} {user.last_name}, thank you for registering in Aqari.'.upper()
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email,]
            send_mail( subject, message, email_from, recipient_list )


            return render(request,"accounts/welcome_email.html",{"user":user})
        except IntegrityError as e:
            msg = f"Please select another username"
        except Exception as e:
            msg = f"something went wrong {e}"

    return render(request, "accounts/register.html",{"msg":msg})
def send_registration_email(user_email):
    subject = 'Welcome to Aqari!'
    message = 'Registration successful. Welcome!'
    from_email = 'moh.q8384@gmail.com'
    recipient_list= [user_email]
    send_mail(subject, message, from_email, recipient_list)
def login_user_view(request: HttpRequest):
    msg = None
    if request.user.is_authenticated:
        return render(request, 'accounts/profile.html')
    elif request.method == "POST":
        
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            
            login(request, user)
            return redirect("accounts:user_profile_view",request.user.id )
        else:
            msg = "Please provide correct username and password"



    return render(request, "accounts/login.html", {"msg" : msg})
def logout_user_view(request: HttpRequest):

    if request.user.is_authenticated:
        logout(request)    

    return redirect("accounts:login_user_view")
def user_profile_view(request: HttpRequest, user_id):
    if not request.user.is_authenticated:
        return render(request, "accounts/login.html")
    try:
        
        user = User.objects.get(id=user_id)
        #properties_owned = Property.objects.filter(owner=user)

    except:
        return render(request, 'main/not_found.html')
    

    return render(request, 'accounts/profile.html', {"user":user})#'properties_owned': properties_owned})
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
                    profile : UserProfile = request.user.userprofile
                except Exception as e:
                    user_profile = UserProfile(user=user, phone=request.POST["phone"],address=request.POST["address"])
                    user_profile.save()

                profile.phone = request.POST["phone"]
                if 'profile_picture' in request.FILES: profile.profile_picture = request.FILES["profile_picture"]
                profile.address = request.POST["address"]
                profile.save()

                return redirect("accounts:user_profile_view", user_id = request.user.id)

            else:
                return redirect("accounts:login_user_view")
        except IntegrityError as e:
            msg = f"Please select another username"
        except Exception as e:
            msg = f"something went wrong {e}"

    return render(request, "accounts/update.html", {"msg" : msg})
def delete_account_view(request:HttpRequest,user_id):
    delete_account=User.objects.get(id=user_id)
    delete_account.delete()
    return redirect("main:home_view")