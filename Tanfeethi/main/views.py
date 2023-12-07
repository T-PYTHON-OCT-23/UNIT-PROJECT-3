from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from django.contrib.auth.models import User
from .models import Trip

# Create your views here.

def home_view(request : HttpRequest):
    return render (request , "main/home.html" )


def booking_trip_view(request : HttpRequest):

    if request.method == "POST":
        trip = Trip(_from=request.POST["_from"], _to=request.POST["_to"], departing=request.POST["departing"] , returning=request.POST["returning"]  ,passenge_age=request.POST["passenge_age"] ,_class=request.POST["_class"] )
        trip.save()
    return render(request , "main/booking_trip.html" )