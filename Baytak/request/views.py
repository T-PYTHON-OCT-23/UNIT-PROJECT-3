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
            return redirect("request:confirmRequest", newRequest.id)
    
        
    
def veiwRequest(request: HttpRequest):
    try:
        
        requests = Request.objects.filter(user = request.user)

        return render(request, 'request/userRequest.html', {"requests" : requests})
    except Exception as e:

        return render(request, "main/not_found.html")
    

def allRequest(request: HttpRequest):
      if "category" in request.GET and request.GET["category"] =="Electrician and Plumber":
            allRequest = Service.objects.filter(category__contains ="Electrician and Plumber")

      elif "category" in request.GET and request.GET["category"] =="Clining":
            allRequest = Service.objects.filter(category__contains ="Clining")

      elif "category" in request.GET and request.GET["category"] =="Water filling":
            allRequest = Service.objects.filter(category__contains ="Water filling")
            
      elif "category" in request.GET and request.GET["category"] =="Moving furniture":
            allRequest = Service.objects.filter(category__contains ="Moving furniture")
      else:
            allRequest = Request.objects.order_by('-createdAt')
     
     
      return render(request ,"request/allRequests.html" , {"allRequest" : allRequest})

def confirmRequest(request: HttpRequest, request_id):
  try: 
   
    newrequest=Request.objects.get(id = request_id)
    
   
    if request.method == 'POST':
        newrequest.isDone = request.POST["isDone"]
        newrequest.save()
        
        return redirect("main:thank")
     

  except Exception as e:
      return redirect("main:not_found_view",{"msg":e})
  
  return render(request ,"request/confirmRequest.html",{"request":newrequest})
def deleteRequest(request : HttpRequest , requset_id):
     
        try:
            request = Request.objects.get(id = requset_id)
            request.delete()
            return redirect("request:allRequest")
        
        except  Exception as e:

         return render(request, "main/not_found.html")

     







