from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Store, Menu,StoreReview ,MenuRequest

# Create your views here.

def add_store_view(request:HttpRequest):
    msg=None
    if request.method=="POST":
        try:
            new_store=Store(name=request.POST["name"],location=request.POST["location"],work_time=request.POST["work_time"],rating=request.POST["rating"])
            if "img" in request.FILES:
                new_store.img=request.FILES["img"]
            new_store.save()
            return redirect("delivery:home_store_view")
        except Exception as e:
            msg = f"An error occured, please fill in all fields and try again . {e}"


    return render(request ,"delivery/add_store.html" ,{"msg":msg})


def home_store_view(request:HttpRequest):

    stores=Store.objects.all()

    return render(request,"delivery/home_store.html",{"stores":stores})

def store_details_view(request:HttpRequest, store_id):
    msg=None
    details=Store.objects.get(id=store_id)
    store=Menu.objects.filter(menu_store=details)

    if request.method=="POST":
        try:
            if not request.user.is_authenticated:
                return render(request, "main/not_authenticated.html", status=401)
            review =StoreReview(store_review=details,user=request.user,rating=request.POST["rating"],comment=request.POST["comment"])
            review.save()
        except Exception as e:
            msg=f"An error occurred, try again .{e}"

    reviews=StoreReview.objects.filter(store_review=details)

    return render(request , "delivery/details_store.html", {"store":details , "stores":store ,"reviews": reviews, "msg":msg})


def delete_store_views(request:HttpRequest, store_id):
    store= Store.objects.get(id=store_id)
    store.delete()

    return redirect("delivery/home_store.html")


def add_menu_view(request:HttpRequest,store_id):
    msg=None
    store=Store.objects.get(id=store_id)

    if request.method=="POST":
        try:
        
            new_menu=Menu(menu_store=store,name=request.POST["name"],description=request.POST["description"], price=request.POST["price"])
            if "img" in request.FILES:
                new_menu.img=request.FILES["img"]
                new_menu.save()
            return redirect("delivery:store_details_view", store_id=store.id)
        except Exception as e:
            msg = f"An error occured, please fill in all fields and try again . {e}"
    

    return render (request,"delivery/add_menu.html", {"store" : store ,"msg":msg})


def update_store_views(request:HttpRequest,store_id):
    msg=None
    store= Store.objects.get(id=store_id)

    if request.method=="POST":
        try:
            store.name=request.POST["name"]
            store.location=request.POST["location"]
            store.work_time=request.POST["work_time"]
            store.rating=request.POST["rating"]
            store.img=request.FILES["img"]
            store.save()

            return redirect("delivery:store_details_view",store_id=store.id)
        except Exception as e:
            msg = f"An error occured, please fill in all fields and try again . {e}"

        
    return render(request,"delivery/update_store.html",{"stores":store , "msg":msg})


def add_menu_request_view(request:HttpRequest, menu_id):

    menu=Menu.objects.get(id=menu_id)
   

    if request.method=="POST":
        new_request=MenuRequest(user=request.user,menu=menu,note=request.POST["note"])
        new_request.save()  
        return redirect("main:order_view" ,new_request.id)
    
    

def menu_request_view(request:HttpRequest):
    try:
        
        my_request_stable=MenuRequest.objects.filter(user=request.user)

        return render(request, "users/profile.html" ,{"requests":my_request_stable})
    except Exception as e:
        return render(request, "main/not_found.html")