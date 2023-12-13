from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from car.models import Car,Rental,Review



# Create your views here.

def home_view(request: HttpRequest):
    #accessing the logged in user info
    if request.user.is_authenticated:
        print(request.user.first_name)

    car = Car.objects.all().order_by("-price")[0:4]
    reviews = Review.objects.all().order_by("-rating")[0:4]


    return render(request, "main/home.html", {"car" : car, "reviews" : reviews})



def about_page_view(request:HttpRequest):

    return render(request,"main/about.html")

def contact_page_view(request:HttpRequest):

    return render(request,"main/contact.html")
