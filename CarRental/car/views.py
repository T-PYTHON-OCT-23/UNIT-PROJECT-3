from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpRequest,HttpResponse
from datetime import datetime
from .models import Car, Rental , Review
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger 
from django.db.models import Q

# Create your views here.


def add_car_view(request : HttpRequest):
    if request.method == "POST":
        car = Car(
            name=request.POST["name"],
            year=request.POST["year"],
            image=request.FILES["image"],
            available=request.POST["available"],
            vehicle_class=request.POST["vehicle_class"],
            vehicle_type=request.POST["vehicle_type"],
            color=request.POST["color"],
            seats=request.POST["seats"],
            pags=request.POST["pags"],
            air_conditioner=request.POST["air_conditioner"],
            transmission_type=request.POST["transmission_type"],
            fuel_type=request.POST["fuel_type"],
            price=request.POST["price"],
            city=request.POST["city"],
        )
        car.save()
        return redirect("car:cars_view")

    air_conditioner_choices = Car.AIR_CONDITIONER_CHOICES
    transmission_type_choices = Car.TRANSMISSION_TYPE_CHOICES
    fuel_type_choices = Car.FUEL_TYPE_CHOICES
    vehicle_class_choices = Car.VEHICLE_CLASS_CHOICES
    vehicle_type_choices = Car.VEHICLE_TYPE_CHOICES
    price_choices = Car.PRICE_CHOICES

    return render(
        request,
        "car/add.html",
        {
            "air_conditioner_choices": air_conditioner_choices,
            "transmission_type_choices": transmission_type_choices,
            "fuel_type_choices": fuel_type_choices,
            "vehicle_class_choices": vehicle_class_choices ,
            "vehicle_type_choices": vehicle_type_choices,
            "price_choices": price_choices
        },
    )


def cars_view(request):
    cars = Car.objects.all().order_by("price") #cars = Car.objects.filter(available = True)
    number_of_cars = Car.objects.all().count()
 
    page = request.GET.get('page')
    # Set the number of items per page
    number_of_items = 3

    # Create a Paginator object
    paginator = Paginator(cars, number_of_items)

    try:
        cars = paginator.page(page)
    except PageNotAnInteger :
        page=1
        # Get the specified page
        cars = paginator.page(page)
    except EmptyPage: 
        cars = paginator.page(paginator.num_pages) 
        cars = paginator.page(page)  


    air_conditioner_choices = Car.AIR_CONDITIONER_CHOICES
    transmission_type_choices = Car.TRANSMISSION_TYPE_CHOICES
    fuel_type_choices = Car.FUEL_TYPE_CHOICES
    vehicle_class_choices = Car.VEHICLE_CLASS_CHOICES
    vehicle_type_choices = Car.VEHICLE_TYPE_CHOICES
    price_choices = Car.PRICE_CHOICES

    context =  {
            "air_conditioner_choices": air_conditioner_choices,
            "transmission_type_choices": transmission_type_choices,
            "fuel_type_choices": fuel_type_choices,
            "vehicle_class_choices": vehicle_class_choices ,
            "vehicle_type_choices": vehicle_type_choices,
            "price_choices": price_choices,
            "cars":cars,
            "number_of_cars":number_of_cars,
            "paginator":paginator
        }
    return render(request, "car/cars.html", context)


def cars_details_view(request:HttpRequest, pk):
    car = Car.objects.get(id=pk)

    reviews = Review.objects.filter(car=car)

    air_conditioner_choices = Car.AIR_CONDITIONER_CHOICES
    transmission_type_choices = Car.TRANSMISSION_TYPE_CHOICES
    fuel_type_choices = Car.FUEL_TYPE_CHOICES
    vehicle_class_choices = Car.VEHICLE_CLASS_CHOICES
    vehicle_type_choices = Car.VEHICLE_TYPE_CHOICES
    price_choices = Car.PRICE_CHOICES


    context= {
            "air_conditioner_choices": air_conditioner_choices,
            "transmission_type_choices": transmission_type_choices,
            "fuel_type_choices": fuel_type_choices,
            "vehicle_class_choices": vehicle_class_choices ,
            "vehicle_type_choices": vehicle_type_choices,
            "price_choices": price_choices
        }
    return render(request, "car/cars_details.html", {"car": car , "reviews":reviews , "context":context})


def cars_update_view(request:HttpRequest, pk):
    
    car = Car.objects.get(id =pk)
    if request.method == "POST":
        car.name =request.POST["name"]
        car.year=request.POST["year"]
        car.image=request.FILES["image"]
        car.vehicle_class=request.POST["vehicle_class"]
        car.vehicle_type=request.POST["vehicle_type"]
        car.color=request.POST["color"]
        car.seats=request.POST["seats"]
        car.pags=request.POST["pags"]
        car.air_conditioner=request.POST["air_conditioner"]
        car.transmission_type=request.POST["transmission_type"]
        car.fuel_type=request.POST["fuel_type"]
        car.price=request.POST["price"]
        car.save()
        return redirect("car:cars_view")

    air_conditioner_choices = Car.AIR_CONDITIONER_CHOICES
    transmission_type_choices = Car.TRANSMISSION_TYPE_CHOICES 
    fuel_type_choices = Car.FUEL_TYPE_CHOICES
    vehicle_class_choices = Car.VEHICLE_CLASS_CHOICES
    vehicle_type_choices = Car.VEHICLE_TYPE_CHOICES
    price_choices = Car.PRICE_CHOICES

    return render(
        request,
        "car/update.html",
        {
            "air_conditioner_choices": air_conditioner_choices,
            "transmission_type_choices": transmission_type_choices,
            "fuel_type_choices": fuel_type_choices,
            "vehicle_class_choices": vehicle_class_choices ,
            "vehicle_type_choices": vehicle_type_choices,
            "price_choices": price_choices,
            "car":car
        },
    )


def cars_delete_view(request:HttpRequest, pk):
 
    car = Car.objects.get(id =pk)
    car.delete()
    return redirect("car:cars_view")



def car_search_view(request:HttpRequest):
    if request.method == "GET":
        query =request.GET.get("query")
        base_query = Q()
        if query:
            base_query &= Q(name__icontains=query)
            cars = Car.objects.filter(base_query)
        else:
            cars = Car.objects.all()
        
    return render(request,"car/search.html",{"cars":cars}) 


def booking_search_view(request:HttpRequest):
    if request.method == "GET" and "city" in request.GET:
        city =request.GET.get("city")
        vehicle_class = request.GET.get("vehicle_class")
        vehicle_type = request.GET.get("vehicle_type")

        cars = Car.objects.filter(city=city, available=True,vehicle_class=vehicle_class,vehicle_type=vehicle_type)

    else:
        cars = []

    context = {
        'cars': cars,
    }

    return render(request, 'car/booking_search.html', context)
    

def add_review_view(request: HttpRequest, pk):

    if request.method == "POST":
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        if not request.user.is_authenticated:
            return render(request, "main/not_authorized.html", status=401)
        
        car_obj = Car.objects.get(id=pk)
        new_review = Review(car=car_obj, reviewer=request.user,rating=rating, comment=comment)  
        new_review.save()
        return redirect("car:cars_details_view", pk =car_obj.id)
    
    return render(request, "car/cars_details.html")
