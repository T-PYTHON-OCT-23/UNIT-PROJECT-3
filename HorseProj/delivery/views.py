from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Store, Menu
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
    store=Menu.objects.filter(menu_store=details)

    return render(request , "delivery/details_store.html", {"store":details , "stores":store})


def delete_store_views(request:HttpRequest, store_id):
    store= Store.objects.get(id=store_id)
    store.delete()

    return redirect("delivery/home_store.html")


def add_menu_view(request:HttpRequest,store_id):
    store=Store.objects.get(id=store_id)

    if request.method=="POST":
        
        new_menu=Menu(menu_store=store,name=request.POST["name"],description=request.POST["description"], price=request.POST["price"])
        if "img" in request.FILES:
            new_menu.img=request.FILES["img"]
            new_menu.save()
        return redirect("delivery:store_details_view", store_id=store.id)
    

    return render (request,"delivery/add_menu.html", {"store" : store})
