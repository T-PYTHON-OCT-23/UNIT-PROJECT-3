from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import StableHorses, ServicesStable
# Create your views here.

def add_stable_views(request:HttpRequest):
    if request.method =="POST":
        new_stable=StableHorses(name=request.POST["name"],city=request.POST["city"],description=request.POST["description"],rating=request.POST["rating"])
        if "img" in request.FILES:
            new_stable.img=request.FILES["img"]
        new_stable.save()
        return redirect ("horses:home_stable_view")

    return render(request, "horses/add_stable.html")



def home_stable_view(request:HttpRequest):

    stables=StableHorses.objects.all()

    return render(request,"horses/home_stable.html",{"stables":stables})


def stable_details_view(request:HttpRequest, stable_id):

    details=StableHorses.objects.get(id=stable_id)
    services=ServicesStable.objects.filter(service=details)

    return render(request , "horses/details_stable.html", {"stable":details , "services":services})

def add_services_view(request:HttpRequest):

    if request.method=="POST":
        stable=StableHorses.objects.get(id=stable_id)
        new_services=ServicesStable(stbleHorse=stable,name_Servic=request.POST["name_Servic"],description_Servic=request.POST["description_Servic"],duration_service=request.POST["duration_service"], price=request.POST["price"])
        new_services.save()
        return redirect("horses:stable_details_view", stable_id=stable.id)
     


