from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Request
from services.models import Service
# Create your views here.


def addRequest(request:HttpRequest, service_id):

    service = Service.objects.get(id = service_id)  
    if request.method == "POST":
        newRequest = Request(user = request.user, service = service, orderTime = request.POST["orderTime"])
        newRequest.save()

    
      

    return redirect("main:thank")
    
    
def veiwRequest(request: HttpRequest):
    
    requests = Request.objects.filter(user = request.user)

    return render(request, 'request/userRequest.html', {"requests" : requests})
    








