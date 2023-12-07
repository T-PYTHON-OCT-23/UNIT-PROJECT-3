from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trip(models.Model):

    trips= models.TextChoices('trips' , ["Riyadh" ,"Doha" ,"Khobar" ,"Muscat"])
    class_choices = models.TextChoices('class_choices' , ["Guest" ,"Business" ,"First" ])
    passenges_age = models.TextChoices("passenges_age" , ["Adults" , "Children" , "infants" , "infant on seat"])

    # A relationship between the passenger and his flight or the flight and the passengers
    passenger=models.ManyToManyField(User)


    _from = models.CharField(max_length=20 , choices = trips.choices , default="Riyadh")
    _to = models.CharField(max_length=20 , choices = trips.choices , default="Doha")
    departing = models.DateField()
    returning = models.TimeField()
    passenge_number = models.IntegerField() 
    passenge_age= models.CharField(max_length=20 , choices = passenges_age.choices , default="Adults")
    _class = models.CharField(max_length=10 , choices = class_choices.choices , default="Guest")


    # round_trip =
    # one_way=
    # multi_city=

    def __str__(self) -> str:
        return f" from {self._from} + to {self._to} number of passenger is: {self.passenge_number}"
    




# from django.db import models


# # Create your models here.

# class Airport(models.Model):#also optoinal
#     code = models.CharField(max_length=3, unique=True)
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.code} - {self.name}"
    


# class Airplane(models.Model):#optional it depend on your project
#     name = models.CharField(max_length=100)
#     capacity = models.PositiveIntegerField()

#     def __str__(self):
#         return self.name
    



# class Flight(models.Model):#flight detailes
#     departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
#     arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
#     departure_time = models.DateTimeField()
#     arrival_time = models.DateTimeField()
#     airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.departure_airport} to {self.arrival_airport} - {self.departure_time}"
    


# class Passenger(models.Model):#passenger information
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
    


# class Reservation(models.Model):#reservation and relation with flight and passenger
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
#     passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
#     seat_number = models.CharField(max_length=10)

#     def __str__(self):
#         return f"{self.passenger} on {self.flight} - Seat {self.seat_number}"