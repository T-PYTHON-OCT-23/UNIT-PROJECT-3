from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path('' , views.home_view , name='home_view'),
    path('booking/trip/' , views.booking_trip_view , name='booking_trip_view'),
    path('add/trip/' , views.add_trip_view , name='add_trip_view'),


]