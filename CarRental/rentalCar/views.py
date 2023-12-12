from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpRequest,HttpResponse
from datetime import datetime
from car.models import Car, Rental

# Create your views here.

def rental_car_view (request:HttpRequest):

    if request.method == "GET":
        #rental_pickup_location = request.GET.get("rental_pickup_location")
        rental_return_location = request.GET.get("rental_return_location")
        rental_pickup_Datetime = request.GET.get("rental_pickup_Datetime")
        rental_return_Datetime = request.GET.get("rental_return_Datetime")
        total_cost = request.GET.get("total_cost")

        rental = Rental.objects.filter(
            rental_return_location=rental_return_location,
            rental_pickup_Datetime=rental_pickup_Datetime,
            rental_return_Datetime=rental_return_Datetime,
            total_cost=total_cost
        )


    else:
        rental = []

    context = {
        'rental': rental,
    }

    return render(request,"rentalCar/rental_car.html",context)