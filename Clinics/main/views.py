from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic, Review, Contact
# Create your views here.


def home_view(request: HttpRequest):

    return render(request, "main/home.html")


def add_clinic(request: HttpRequest):
    if request.method == "POST":
        new_clinic = Clinic(name=request.POST["name"], about=request.POST["about"],
                            category=request.POST["category"], image=request.FILES["image"], location=request.POST["location"])
        new_clinic.save()
        return redirect("main:display")

    return render(request, "main/add_clinic.html", {"categories": Clinic.categories})


def display(request: HttpRequest):

    clinic = Clinic.objects.all()
    return render(request, "main/display.html", {"clinic": clinic})


def detail_clinic(request: HttpRequest, clinic_id):

    clinic_detail = Clinic.objects.get(id=clinic_id)
    return render(request, "main/detail.html", {"clinic": clinic_detail})



def about_clinic(request: HttpRequest):

    return render(request, "main/about_us.html")


def contact(request: HttpRequest):
    if request.method == "POST":
        new_ask = Contact(user_name=request.POST["user_name"], email=request.POST["email"],
                          message=request.POST["message"])
        new_ask.save()
        return redirect("main:contact")

    return render(request, "main/contact.html")
