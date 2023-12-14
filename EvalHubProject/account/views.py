from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from evalhub.models import CustomUser
from django.contrib.auth.models import User
from django.db import IntegrityError

def register_user_view(request: HttpRequest):
    msg = None
    if request.method == "POST":
        try: 
            user: User = User.objects.create_user(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
            user.save()

            c_user: CustomUser= CustomUser(user=user)
            c_user.save()
            return redirect("account:login_user_view")
        except IntegrityError as e:
            msg = f"Please select another username"
        except Exception as e:
            msg = f"something went wrong {e}"

    return render(request, 'account/register.html', {"msg" : msg}) 

def login_user_view(request: HttpRequest):
    msg = None
    if request.method == "POST":
        try:
            user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

            if user:
                login(request, user)
                return redirect("account:home_page_view")
            else:
                msg = "Please provide correct username and password"

        except Exception as e:
                msg = f"something went wrong {e}"

    return render(request, 'account/login.html', {"msg" : msg}) 

def logout_user_view(request: HttpRequest):
    logout(request)
    return redirect('account:login_user_view')  


def user_profile_view(request: HttpRequest, user_id):
    user = request.user

    return render(request, 'account/user_profile.html', {'user': user})  

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

                return redirect("account:user_profile_view", user_id = request.user.id)

            else:
                return redirect("accounts:login_user_view")
        except IntegrityError as e:
            msg = f"Please select another username"
        except Exception as e:
            msg = f"something went wrong {e}"

    return render(request, 'account/update_user.html', {"msg" : msg})  
