from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    """
    Represents a car available for rental.
    """
    AIR_CONDITIONER_CHOICES = (
        ('Standard', 'Standard'),
        ('Climate Control', 'Climate Control'),
        ('Dual-Zone Climate Control', 'Dual-Zone Climate Control'),
    )
    TRANSMISSION_TYPE_CHOICES = (
        ("Automatic", 'Automatic'),
        ("Manual", 'Manual'),
    )
    FUEL_TYPE_CHOICES = (
        ('Diesel', 'Diesel'),
        ('Petrol', 'Petrol'),
    )
     
    CITY_TYPE_CHOICES = (
        ("Riyadh", 'Riyadh'),
        ("Abha", 'Abha'),
        ("Khobar", 'Khobar'),
        ("Hail", 'Hail'),
        ("Jeddah", 'Jeddah'),
    )

    VEHICLE_CLASS_CHOICES = (
        ("Economic","Economic"),
        ("Middle Class","Middle Class"),
        ("Top Grade","Top Grade"),
        ("Luxury","Luxury"),
    )

    VEHICLE_TYPE_CHOICES = (
        ("Sedan","Sedan"),
        ("SUV","SUV"),
        ("VAN","VAN"),
    )

    PRICE_CHOICES = (
        (0-200,0-200),
        (200-600,200-600),
        (800,800),
    )

    #rental_company = models.ForeignKey(RentalCompany, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=512,default="")
    year = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    available = models.BooleanField(default=True)
    vehicle_class = models.TextField(choices=VEHICLE_CLASS_CHOICES, default=1)
    vehicle_type = models.TextField(choices=VEHICLE_TYPE_CHOICES, default=1)
    color = models.CharField(max_length=20, default="")
    seats = models.PositiveIntegerField()
    pags = models.PositiveIntegerField()
    air_conditioner = models.TextField(choices=AIR_CONDITIONER_CHOICES, default=1)  # Default to 'Standard'
    transmission_type = models.TextField(choices=TRANSMISSION_TYPE_CHOICES, default=1)
    fuel_type = models.TextField(choices=FUEL_TYPE_CHOICES, default=1)
    price = models.PositiveIntegerField(choices=PRICE_CHOICES, default=200)
    city = models.CharField(max_length=124, choices=CITY_TYPE_CHOICES, default="Riyadh")

    def __str__(self):
        return f"{self.name} {self.year} {self.vehicle_class} {self.available}"


class Rental(models.Model):
    """
    Represents a rental transaction.
    """
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_pickup_location = models.CharField(max_length=512,default="")
    rental_return_location = models.CharField(max_length=512,default="")
    rental_pickup_Datetime = models.DateTimeField(auto_now_add=True)
    rental_return_Datetime = models.DateTimeField(auto_now_add=True)
    total_cost = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)

    

    def __str__(self):
        return f"{self.renter.username} - {self.car} - from {self.rental_pickup_Datetime} to {self.rental_return_Datetime}"


class Review(models.Model):
    """
    Represents a review for a rented car.
    """
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default="")
    comment = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.car} - {self.rating} stars"
    

class RentalCompany(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name
    