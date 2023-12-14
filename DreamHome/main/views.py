from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from products.models import Product,Review
# Create your views here.

def home_view(request: HttpRequest):

    #if request.user.is_authenticated:
       # print(request.user.first_name)

   # movies = Movie.objects.all().order_by("-release_date")[0:4]
   # reviews = Review.objects.all().order_by("-rating")[0:4]


    return render(request, "main/home.html")


def not_found_view(request: HttpRequest):

   
    return render(request, "main/not_found.html")



