from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from .models import Reservation , Flight
from django.contrib.auth.models import User
from django.db import transaction # meaning : to ensure all the operations are executed successfully, or none of them are.
from datetime import datetime 
# from django.db.models import Sum


# Create your views here.

def home_view(request : HttpRequest):
    trips=Flight.objects.all()
    return render (request , "main/home.html" , {"trips":trips} )






@transaction.atomic
def booking_trip_view(request : HttpRequest):
    msg=None
    trips = Flight.objects.all()

    if request.method == "POST":
        try:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            trip_time = request.POST.get("trip_time")

            # Validate that all required fields are present
            if not (first_name and last_name and email):
                raise ValueError("All fields are required.")

            # Convert the trip_time string to datetime (adjust the format based on your needs)
            trip_datetime = datetime.strptime(trip_time, "%Y-%m-%d %H:%M:%S")

            passenger = User(first_name=first_name, last_name=last_name, email=email)
            passenger.save()

            flight = Flight(departure_time=trip_datetime, arrival_time=trip_datetime)
            flight.save()

            reservation = Reservation(passenger=passenger, flight=flight)
            reservation.save()

            # Redirect after successful form submission
            
            return redirect("main:confirmation_page")  

        except Exception as e:
            msg = f"An error occurred: {str(e)}"
            return render(request, "main/booking_trip.html", {"trips": trips, "msg": msg})

    return render(request, "main/booking_trip.html", {"trips": trips})




from django.contrib.auth.decorators import login_required

@login_required
def confirmation_page(request:HttpRequest):
    try:
        reservation = Reservation.objects.get(passenger=request.user)
        booked_trip_id = reservation.flight.id
    except Reservation.DoesNotExist:
        booked_trip_id = None
    confirmation_data = {
        'trip_id': booked_trip_id,
        'departure_time': '2023-12-01 10:00:00',
        'arrival_time': '2023-12-01 12:00:00',
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,



    }

    return render(request, "main/confirmation_page.html", {'confirmation_data': confirmation_data})









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
            return redirect("main:booking_trip_view")  
   

    return render(request, "main/add_trip.html" )