from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import consultation ,consultationRequest
from django.contrib.auth.models import User
# Create your views here.


def consultation_views(request:HttpRequest,user_id):
    user=User.objects.get(id=user_id)
    if request.method=="POST":
        
        new_consultation=consultation(user=user,category=request.POST["category"],title=request.POST["title"],description=request.POST["description"],age_horse=request.POST["age_horse"],horse_type=request.POST["horse_type"])
        new_consultation.save()
       

        
    
    return render(request, "Consultations/my_consultation.html",{"user":user , "categories" : consultation.categories})


def add_consultation_request_view(request:HttpRequest):

    consultation=consultation.objects.all()
   

    if request.method=="POST":
        new_request=consultationRequest(user=request.user,consultation=consultation,note=request.POST["note"])
        new_request.save()  
        return redirect("main:order_view" ,new_request.id)
    
    
    return render( request, "Consultations\my_consultation.html")
    
    

def consultation_request_view(request:HttpRequest):
    try:
        
        my_request_stable=consultationRequest.objects.filter(user=request.user)

        return render(request, "users/profile.html" ,{"requests":my_request_stable})
    except Exception as e:
        return render(request, "main/not_found.html")