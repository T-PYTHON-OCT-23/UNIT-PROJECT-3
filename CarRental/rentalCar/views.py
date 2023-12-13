from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from car.models import Rental

def rental_car_view(request: HttpRequest):
    if request.method == "GET":
        rental_return_location = request.GET.get("rental_return_location")
        rental_pickup_Datetime_str = request.GET.get("rental_pickup_Datetime")
        rental_return_Datetime_str = request.GET.get("rental_return_Datetime")
        total_cost = request.GET.get("total_cost")

        # Check if pickup and return datetimes are not None
        if rental_pickup_Datetime_str is not None and rental_return_Datetime_str is not None:
            try:
                rental_pickup_Datetime = datetime.strptime(rental_pickup_Datetime_str, "%Y-%m-%d")
                rental_return_Datetime = datetime.strptime(rental_return_Datetime_str, "%Y-%m-%d")

                try:
                    rental = Rental.objects.get(
                        rental_return_location=rental_return_location,
                        rental_pickup_Datetime=rental_pickup_Datetime,
                        rental_return_Datetime=rental_return_Datetime,
                        total_cost=total_cost
                    )
                except Rental.DoesNotExist:
                    rental = None

            except ValueError:
                # Handle the case where strptime fails (e.g., due to an incorrect date format)
                rental = None
        else:
            rental = None

    else:
        rental = None

    context = {
        'rental': rental,
    }

    return render(request, "rentalCar/rental_car.html", context)
