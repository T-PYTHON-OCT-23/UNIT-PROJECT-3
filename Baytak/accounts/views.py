from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import Profile

def registerPage(request: HttpRequest):
    message = None


    if request.method == "POST":
      try:
        newUser = User.objects.create_user(username = request.POST["username"], first_name = request.POST["first_name"], last_name = request.POST["last_name"], email = request.POST["email"], password = request.POST["password"])
        newUser.save()

        userProfile = Profile(user = newUser, avatar = request.FILES["avatar"])
        userProfile.save()
        return redirect("accounts:loginUser")
      except IntegrityError as e:
         message = "Please select another username"

         
    return render(request, "accounts/register.html", {"message" : message})

def loginUser(request: HttpRequest):
   
   message = None

   if request.method == "POST":
       
       user = authenticate(request, username = request.POST["username"], password = request.POST["password"])
       
       if user:
           login(request, user)
           return redirect("main:homePage")
       
       else:
           message = "Please provide correct username and password"
   return render(request, "accounts/login.html", {"message" : message})


def logoutUser(request: HttpRequest):

   if request.user.is_authenticated:
        logout(request)    

   return redirect("accounts:loginUser") 

def userProfile(request: HttpRequest, user_id):
   try:
        
        user = User.objects.get(id=user_id)

   except:
        return render(request, 'main/not_found.html')
    

   return render(request, 'accounts/profile.html', {"user":user})

def updateProfile():
   pass

