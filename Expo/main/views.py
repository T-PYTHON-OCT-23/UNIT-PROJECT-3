from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from .models import * 

def home_view(request: HttpRequest):

      if request.user.is_authenticated:
        print(request.user.first_name)
    
      return render(request, "main/home.html")

def riyadh_expo_view(request: HttpRequest):

    
      return render(request, "main/riyadh_expo.html")

