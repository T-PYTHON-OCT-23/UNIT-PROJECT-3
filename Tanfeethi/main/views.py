from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.db import transaction # meaning : to ensure all the operations are executed successfully, or none of them are.
from datetime import datetime 
from django.views.decorators.csrf import csrf_protect

# from django.db.models import Sum


# Create your views here.

def home_view(request : HttpRequest):
    trips = Flight.objects.all()


    sort_by = request.GET.get('sort_by', None)

    if sort_by in ['price', '-price']:
        trips = trips.order_by(sort_by)

    context = {
        'trips': trips,
        'sort_by': sort_by,

    }

    return render(request, 'main/home.html', context)


@transaction.atomic
@csrf_protect
def booking_trip_view(request:HttpRequest, trip_id ):
    msg=None
    trips = Flight.objects.get(id=trip_id)
    try:
        if request.method == "POST":
            if request.user.is_authenticated:
                user=request.user
            #  if not (username and first_name and last_name and email and trip_time_str):
            #      raise ValueError("All fields are required.")

                reservation = Reservation(passenger=user, trips=trips,first_name=first_name,last_name=last_name)
                reservation.save()

                if trips.seat_number > 0:
                    first_name = request.POST["first_name"]
                    last_name = request.POST["last_name"]

                    trips.seat_number -= 1
                    trips.save()
                    
                    msg = "Trip booked successfully!"
                    return redirect("main:home_view")
                else:
                    msg = "No available seats for this flight."


                msg = "Trip booked successfully!"
                return redirect( "main:home_view")

    except Exception as e:
        msg = f"An error occurred: {str(e)}"
        return render(request, "main/error_page.html", {"trips": trips})
    
    return render(request, "main/booking_trip.html", {"trips": trips,"msg":msg})








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
    cities = City.objects.all()

   
    if request.method == "POST":
        departure_time = request.POST.get("departure_time")
        arrival_time = request.POST.get("arrival_time")
        price = request.POST.get("price")
        seat_number = request.POST.get("seat_number")

        if departure_time and arrival_time:
            flight = Flight(departure_time=departure_time, arrival_time=arrival_time , price=price , seat_number=seat_number)
            flight.save()
            return redirect("main:home_view")  
    context={
        'cities':cities,
    }
   

    return render(request, "main/add_trip.html"  , context)



# def add_city_view(request:HttpRequest):
#     new_city = City(name='New City')
#     new_city.save()
#     return HttpResponse('New city added successfully!')



def error_page_view(request : HttpRequest):
    return render(request , "main/error_page.html")





