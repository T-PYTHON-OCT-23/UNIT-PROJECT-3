from django.db import models


# Create your models here.



class Flight(models.Model):#flight detailes


    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()


    def __str__(self):
        return f"Arrival time: {self.arrival_time} - {self.departure_time}"
    


class Passenger(models.Model):#passenger information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Passenger name : {self.first_name} {self.last_name}"
    

class Reservation(models.Model):#reservation and relation with flight and passenger
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    seat_number = models.CharField(max_length=10)


    def __str__(self):
        return f"Reservation : {self.passenger} - {self.seat_number}"
    
# class OneWay(Flight):
