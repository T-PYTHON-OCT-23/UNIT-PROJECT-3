from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Flight(models.Model):#flight detailes
    departure_city = models.ForeignKey(City, related_name='departures', on_delete=models.CASCADE )
    arrival_city = models.ForeignKey(City, related_name='arrivals', on_delete=models.CASCADE )
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    seat_number = models.CharField(max_length=10,null=True)


    def duration(self):
        return self.arrival_time - self.departure_time


    def __str__(self):
        return f"{self.departure_city} to {self.arrival_city} at: {self.arrival_time.strftime('%Y-%m-%dT%H:%M')} - {self.departure_time.strftime('%Y-%m-%dT%H:%M')}  Duration: {self.duration()}"
    
    


# class Passenger(models.Model):#passenger information
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return f"Passenger name : {self.first_name} {self.last_name}"
    

class Reservation(models.Model):#reservation and relation with flight and passenger
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    def __str__(self):
        return f"Reservation : {self.passenger} - {self.flight}"
    
# class OneWay(Flight):
