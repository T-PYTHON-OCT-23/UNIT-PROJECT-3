from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.db import transaction # meaning : to ensure all the operations are executed successfully, or none of them are.
from datetime import datetime 
from django.views.decorators.csrf import csrf_protect
from django.db.models import Min


# Create your views here.

def home_view(request : HttpRequest):
    trips = Flight.objects.all()

    sort_by = request.GET.get('sort_by', None)

    if sort_by in ['price', '-price' ]:
        trips = trips.order_by(sort_by)
    
    if sort_by in [ 'departure_time' , '-departure_time']:
        trips = trips.order_by(sort_by)

    context = {
        'trips': trips,
        'sort_by': sort_by,
    }

    return render(request, 'main/home.html', context)



@transaction.atomic
@csrf_protect
def booking_trip_view(request:HttpRequest, trip_id ):
    if not request.user.is_authenticated:
        return redirect("account:login_view")
    msg=None
    trips = Flight.objects.get(id=trip_id)
    try:
        if request.method == "POST":
            user = request.user
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]

            reservation = Reservation(passenger=user, flight=trips, first_name=first_name, last_name=last_name)
            reservation.save()

            if trips.seat_number > 0:
                trips.seat_number = trips.seat_number - 1
                trips.save()
                msg = "Trip booked successfully!"
                return redirect("main:payment_view" , trip_id=trips.id)
            else:
                msg = "No available seats for this flight."


    except Exception as e:
        msg = f"An error occurred: {str(e)}"

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
    if not request.user.is_staff:
        return redirect("main:error_page_view")
    cities = City.objects.all()

   
    if request.method == "POST":
        departure_time = request.POST.get("departure_time")
        arrival_time = request.POST.get("arrival_time")
        price = request.POST.get("price")
        seat_number = request.POST.get("seat_number")
        arrival_city = request.POST.get("arrival_city")
        departure_city=request.POST.get("departure_city")

        try:
            price = float(price)
            seat_number = int(seat_number)
        except (TypeError, ValueError):
            return HttpResponse("Invalid price or seat_number", status=400)
        
        try:
            arrival_city = City.objects.get(id=arrival_city)
            departure_city = City.objects.get(id=departure_city)
        except City.DoesNotExist:
            return HttpResponse("Invalid arrival_city or departure_city", status=400)


        if departure_time and arrival_time:
            flight = Flight(departure_time=departure_time, arrival_time=arrival_time , price=price , seat_number=seat_number , arrival_city = arrival_city , departure_city=departure_city)
            flight.save()
            return redirect("main:home_view")  
    context={
        'cities':cities,
    }
   
    return render(request, "main/add_trip.html"  , context)





def search_view(request:HttpRequest):
    keyword = request.GET.get("search", "")
    cities = Flight.objects.filter(arrival_city__name__icontains=keyword) | Flight.objects.filter(departure_city__name__icontains=keyword)
    context = {"cities": cities, "keyword": keyword}
    return render(request, "main/search_results.html", context)





def payment_view(request:HttpRequest , trip_id):
    if not request.user.is_authenticated:
        return redirect("account:login_view")
    
    trip = Flight.objects.get(id = trip_id)
    return render(request , "main/payment.html" , {"trip" : trip})


def error_page_view(request : HttpRequest):
    return render(request , "main/error_page.html")





