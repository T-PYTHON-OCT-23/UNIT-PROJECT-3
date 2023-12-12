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
        
        return redirect("request:confirmRequest",service_id)
    
        
    
def veiwRequest(request: HttpRequest):
    try:
        
        requests = Request.objects.filter(user = request.user)

        return render(request, 'request/userRequest.html', {"requests" : requests})
    except Exception as e:

        return render(request, "main/not_found.html")
    

def allRequest(request: HttpRequest):
     
     allRequest = Request.objects.order_by('-createdAt')
     return render(request ,"request/allRequests.html" , {"allRequest" : allRequest})

def confirmRequest(request: HttpRequest, service_id):
  try: 
    service = Service.objects.get(id = service_id) 
    if request.method == 'POST':
        confirm = Request( isDone = request.POST["isDone"])
        confirm.save()
        return redirect("main:thank")
     
    return render(request ,"request/confirmRequest.html",{"service":service})

  except Exception as e:

        return render(request, "main/not_found.html")

def deleteRequest(request : HttpRequest , requset_id):
     
        try:
            request = Request.objects.get(id = requset_id)
            request.delete()
            return redirect("request:allRequest")
        
        except  Exception as e:

         return render(request, "main/not_found.html")

     







