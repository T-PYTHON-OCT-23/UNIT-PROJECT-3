from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from .models import Passenger , Reservation , Flight
# from django.db.models import Sum


# Create your views here.

def home_view(request : HttpRequest):
    return render (request , "main/home.html" )


def booking_trip_view(request : HttpRequest):

    if request.method == "POST":
        
        flight = Flight(departure_time=request.POST["departure_time"], arrival_time=request.POST["arrival_time"] )
        flight.save()

        passenger = Passenger(first_name = request.POST["first_name"] , last_name = request.POST["last_name"] , email = request.POST["email"])
        passenger.save()

        reservation = Reservation( passenger=passenger , flight=flight )
        # if 
        reservation.save()

        # flightـduration = Flight.request["departure_time"] - Flight.request["arrival_time"]
        
    return render(request , "main/booking_trip.html" )


def add_trip_view(request : HttpRequest): 

    # if request.method == "POST":
        
    #     flight = Flight(departure_time=request.POST.get("departure_time"), arrival_time=request.POST.get("arrival_time") )
    #     flight.save()

    # return render(request , "main/add_trip.html ")

    if request.method == "POST":
        departure_time = request.POST.get("departure_time")
        arrival_time = request.POST.get("arrival_time")

        if departure_time and arrival_time:
            flight = Flight(departure_time=departure_time, arrival_time=arrival_time)
            flight.save()
            return redirect("main/home.html")  

    return render(request, "main/add_trip.html")