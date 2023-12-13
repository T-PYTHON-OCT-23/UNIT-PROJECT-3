
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from Art.models import Art , Review


# Create your views here.
def home_view(request: HttpRequest):
   
   arts = Art.objects.all()
   reviews = Review.objects.all().order_by("created_at")[0:5]
   
   return render ( request , "main/index.html" ,{"arts" : arts ,"reviews" : reviews}) 



