from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import StableHorses, ServicesStable, Reviews
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
    try:
        details=StableHorses.objects.get(id=stable_id)
        services=ServicesStable.objects.filter(stbleHorse=details)

        if request.method=="POST":
            if not request.user.is_authenticated:
                pass

            reviews=Reviews(horses=details,user=request.user,rating=request.POST["rating"],comment=request.POST["comment"])
            reviews.save()
        reviews=Reviews.objects.filter(horses=details)
    except Exception as e :
        print(e)

    return render(request , "horses/details_stable.html", {"stable":details , "services":services, "reviews":reviews})

def add_services_view(request:HttpRequest,stable_id):
    stable=StableHorses.objects.get(id=stable_id)

    if request.method=="POST":
        
        new_services=ServicesStable(stbleHorse=stable,name_Servic=request.POST["name_Servic"],description_Servic=request.POST["description_Servic"],duration_service=request.POST["duration_service"], price=request.POST["price"])
        new_services.save()
        return redirect("horses:stable_details_view", stable_id=stable.id)
    

    return render (request, "horses/add_services.html", {"stable" : stable})
     
    
def delete_stable_views(request:HttpRequest, stable_id):
    stable= StableHorses.objects.get(id=stable_id)
    stable.delete()

    return redirect( "horses:home_stable_view")

def update_stable_views(request:HttpRequest,stable_id):
    stable= StableHorses.objects.get(id=stable_id)

    if request.method=="POST":
        stable.name=request.POST["name"]
        stable.city=request.POST["city"]
        stable.description=request.POST["description"]
        stable.rating=request.POST["rating"]
        stable.img=request.FILES["img"]
        stable.save()

        return redirect("horses:stable_details_view",stable_id=stable.id)
    
    return render(request,"horses/update_stable.html",{"stable":stable})



# def kkd():

#     my_request_stable = StableREquest.objects.filter(user=request.user)