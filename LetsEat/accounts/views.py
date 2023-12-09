
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import Profile

# Create your views here.

def sign_up_view (request:HttpRequest):
    msg =None
    try:
        if request.method == "POST":
                #create a new user
                user = User.objects.create_user(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
                user.save()
                return redirect("accounts:sign_in_view")
    except Exception as e:
     msg= f"{e}"
     

    return render(request, "accounts/sign_up.html", {"msg" : msg})


def sign_in_view(request:HttpRequest):
    msg=None
# authenticate user
    try:
        if request.method == "POST":
            user = authenticate(request, username=request.POST["username"], password= request.POST["password"])

            if user:
                    login(request, user) #sign in user
                    return redirect("main:home_view")
            else:
                    msg = "Please provide correct username and password"

    except Exception as e:
      msg =f"sothing went wrong {e}"

    return render(request, "accounts/sign_in.html", {"msg" : msg})



def sign_out_view(request: HttpRequest):
   
    if request.user.is_authenticated:
        logout(request)
    
    return redirect("accounts:sign_in_view")
     


# def user_profile_view(request: HttpRequest, user_id ):

#     try: 
#         user = User.objects.get(id=user_id)
#     except:
#         return render(request, 'main/not_found.html')

#     return render(request, 'account/profile1.html', {"user":user})


