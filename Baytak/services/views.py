from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Service , Review


def addServices(request : HttpRequest):

    if request.method == "POST":
        newService = Service(name = request.POST["name"], address = request.POST["address"], image = request.FILES["image"], about = request.POST["about"], nationality = request.POST["nationality"], duration = request.POST["duration"], quantity = request.POST["quantity"], city = request.POST["city"], category = request.POST["category"])
        newService.save()
        return redirect("main:homePage")
    
    

    return render(request, "services/addServices.html" , {"categories" : Service.categories , "durations" : Service.durations})

def viewServices(request : HttpRequest):

    if "category" in request.GET and request.GET["category"] =="Electrician and Plumber":
      service = Service.objects.filter(category__contains ="Electrician and Plumber")

    elif "category" in request.GET and request.GET["category"] =="Clining":
        service = Service.objects.filter(category__contains ="Clining")

    elif "category" in request.GET and request.GET["category"] =="Water filling":
        service = Service.objects.filter(category__contains ="Water filling")
        
    elif "category" in request.GET and request.GET["category"] =="Moving furniture":
        service = Service.objects.filter(category__contains ="Moving furniture")

    return render(request ,"services/viewServices.html" , {"service" : service})

def serviceDetails(request : HttpRequest ,service_id):

    try: 
       service = Service.objects.get(id = service_id)

       if request.method == "POST":
            if not request.user.is_authenticated:
               return render(request, "main/not_authorized.html", status=401)
            userReview = Review( service = service , user = request.user , comment  = request.POST["comment"], rating  = request.POST["rating"] )
            userReview.save()

       userReviews = Review.objects.filter(service = service)
    except  Exception as e:

       return render(request, "main/not_found.html"  )
       
    return render(request ,"services/serviceDetails.html" , {"service" : service , "userReviews" : userReviews })