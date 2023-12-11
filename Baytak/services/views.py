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
    else:
        service=Service.objects.all()
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

def updateService(request : HttpRequest , service_id):
    if not request.user.is_staff:
        return render(request, 'main/not_authorized.html' , status=401)
    try:
            service = Service.objects.get(id = service_id)

            if request.method == "POST":
                service.name = request.POST["name"]
                service.address = request.POST["address"]
                service.about=  request.POST["about"]
                service.image = request.FILES["image"]
                service.nationality = request.POST["nationality"]
                service.city = request.POST["city"]
                service.duration = request.POST["duration"]
                service.quantity = request.POST["quantity"]
                service.category = request.POST["category"]
                
                service.save()

                return redirect( "services:serviceDetails" , service_id = service.id)
    
           
            return render(request ,"services/updateService.html" , {"service" : service , "categories" : Service.categories , "durations" : Service.durations})                    
    except  Exception as e:

       return render(request, "main/not_found.html")
    
    
   

def deleteService(request : HttpRequest , service_id):
     if not request.user.is_staff:
        return render(request, 'main/not_authorized.html' , status=401)
     
     try:
        service = Service.objects.get(id = service_id)
        service.delete()

        return redirect("services:viewServices")
     except  Exception as e:

       return render(request, "main/not_found.html")
       
def searchService(request : HttpRequest):
   if "search" in request.GET:
      nameSearch = request.GET["search"]
      service = Service.objects.filter(name__contains = nameSearch)
   else:
      service = Service.objects.all() 

   return render(request, "services/search.html" ,  {"service" : service}) 