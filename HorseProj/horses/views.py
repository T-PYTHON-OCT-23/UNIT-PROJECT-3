from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import StableHorses, ServicesStable, Reviews,StableRequest
# Create your views here.

def add_stable_views(request:HttpRequest):
    msg=None
    if request.method =="POST":
        try:
            new_stable=StableHorses(name=request.POST["name"],city=request.POST["city"],description=request.POST["description"],rating=request.POST["rating"])
            if "img" in request.FILES:
                new_stable.img=request.FILES["img"]
            new_stable.save()
            return redirect ("horses:home_stable_view")
        except Exception as e:
            msg = f"An error occured, please fill in all fields and try again . {e}"

    return render(request, "horses/add_stable.html" ,{"msg":msg})



def home_stable_view(request:HttpRequest):

    stables=StableHorses.objects.all()

    return render(request,"horses/home_stable.html",{"stables":stables})


def stable_details_view(request:HttpRequest, stable_id):
    try:
        details=StableHorses.objects.get(id=stable_id)
        services=ServicesStable.objects.filter(stbleHorse=details)
        if request.method=="POST":
            if not request.user.is_authenticated:
                return render(request, "main/not_authenticated.html", status=401)

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
    msg=None
    stable= StableHorses.objects.get(id=stable_id)

    if request.method=="POST":
        try:
            stable.name=request.POST["name"]
            stable.city=request.POST["city"]
            stable.description=request.POST["description"]
            stable.rating=request.POST["rating"]
            stable.img=request.FILES["img"]
            stable.save()

            return redirect("horses:stable_details_view",stable_id=stable.id)
        except Exception as e:
             msg = f"An error occured, please fill in all fields and try again . {e}"

        
    return render(request,"horses/update_stable.html",{"stable":stable , "msg":msg})

def search_horses_view(request:HttpRequest):
    if "search" in request.GET:
        return_search=request.GET["search"]
        horse=StableHorses.objects.filter(name__contains=return_search)
    else:
        horse = StableHorses.objects.all()

    return render(request, "horses/search.html",{"horses":horse})


# def kkd():

#     my_request_stable = StableREquest.objects.filter(user=request.user)
#     my_request_stable=StableRequest.objects.filter(user=request.user)

def add_stable_request_view(request:HttpRequest, service_id):

    service=ServicesStable.objects.get(id=service_id)
   

    if request.method=="POST":
        new_request=StableRequest(user=request.user,services=service,note=request.POST["note"])
        new_request.save()  
        return redirect("main:order_view" ,new_request.id)
    


def stable_request_view(request:HttpRequest):
    try:
        
        my_request_stable=StableRequest.objects.filter(user=request.user)

        return render(request, "users/profile.html" ,{"requests":my_request_stable})
    except Exception as e:
        return render(request, "main/not_found.html")

    

   

  



