from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Store
# Create your views here.

def add_store_view(request:HttpRequest):

    if request.method=="POST":
        new_store=Store(name=request.POST["name"],location=request.POST["location"],work_time=request.POST["work_time"],rating=request.POST["rating"])
        if "img" in request.FILES:
            new_store.img=request.FILES["img"]
        new_store.save()
        return redirect("delivery:home_store_view")

    return render(request ,"delivery/add_store.html")


def home_store_view(request:HttpRequest):

    stores=Store.objects.all()

    return render(request,"delivery/home_store.html",{"stores":stores})

def store_details_view(request:HttpRequest, store_id):

    details=Store.objects.get(id=store_id)

    return render(request , "horses/details_stable.html", {"store":details})

