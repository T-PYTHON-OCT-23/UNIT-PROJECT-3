from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Request
from services.models import Service
# Create your views here.


def addRequest(request:HttpRequest, service_id):
        if not request.user.is_authenticated:
               return render(request, "main/not_authorized.html", status=401)
        
        service = Service.objects.get(id = service_id)  
        if request.method == "POST":
            newRequest = Request(user = request.user, service = service, orderTime = request.POST["orderTime"])
            newRequest.save()
        
        return redirect("request:confirmRequest")
    
        
    
def veiwRequest(request: HttpRequest):
    try:
        
        requests = Request.objects.filter(user = request.user)

        return render(request, 'request/userRequest.html', {"requests" : requests})
    except Exception as e:

        return render(request, "main/not_found.html")
    

def allRequest(request: HttpRequest):
     
     allRequest = Request.objects.order_by('-createdAt')
     return render(request ,"request/allRequests.html" , {"allRequest" : allRequest})

def confirmRequest(request: HttpRequest):
     
      return render(request ,"request/confirmRequest.html")


def statusRequest(request:HttpRequest, service_id):
     
     service = Service.objects.get(id = service_id) 
     if request.method == 'POST':
        newRequest = Request(user = request.user, service = service, isDone = request.POST["isDone"])
        newRequest.save()
     

     







