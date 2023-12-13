from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import StableRequest

# Create your views here.


# def add_request_view(request:HttpRequest):

#     if request.method=="POST":
#         new_request=StableRequest(note=request.POST["note"])
#         new_request.save()
#         return redirect("request:my_request_view")
    
#     return render(request, "request/add_request.html")


# def my_request_view(request:HttpRequest):
#     requests=StableRequest.objects.filter(user=request.user)

#     return render(request, "request/....")