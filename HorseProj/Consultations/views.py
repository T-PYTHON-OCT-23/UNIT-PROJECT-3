from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import consultation
from django.contrib.auth.models import User
# Create your views here.


def consultation_views(request:HttpRequest,user_id):
    user=User.objects.get(id=user_id)
    if request.method=="POST":
        
        new_consultation=consultation(user=user,category=request.POST["category"],title=request.POST["title"],description=request.POST["description"],age_horse=request.POST["age_horse"],horse_type=request.POST["horse_type"])
        new_consultation.save()
        return redirect("main:order_view")
       

        
    
    return render(request, "Consultations/my_consultation.html",{"user":user , "categories" : consultation.categories})