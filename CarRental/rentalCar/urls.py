from django.urls import path
from . import views

app_name = "rentalCar"

urlpatterns = [
    path("",views.rental_car_view,name="rental_car_view")
]