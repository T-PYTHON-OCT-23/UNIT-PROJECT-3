from django.shortcuts import render ,redirect
from django.http import HttpRequest , HttpResponse


# Create your views here.

def add_view(request:HttpRequest):
    return render(request,"objectives/add.html")