from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Service
# Create your views here.


def add_service_view(request:HttpRequest):
    massage = ''
    #check here if he a staff 
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                new_services = Service(services_name=request.POST['service_name'],description=request.POST['description'],type=request.POST['type'],image=request.POST['image'],price=request.POST['price'])
                new_services.save()
                redirect('services:show_services_view')

            except Exception as e:
                massage = f"something went wrong{e}"

    return render(request,'services/add_services.html',{"massage":massage})


def show_services_view(request:HttpRequest):
    massage = ''
    # check if the user login
    try:
        service = Service.objects.all()
    except Exception as e:
        massage = f"Something went wrong {e}"

    return render(request,'services/show_services.html',{"massage":massage,"services":service})


def edit_service_view(request:HttpRequest):
    massage = ''
    
    return render(request,'services/edit_services.html',{"massage":massage})


def review_service_view(request:HttpRequest):
    massage = ''

    return render(request,'services/review_service.html',{"massage":massage})

def service_detils_view(request:HttpRequest):
    massage = ''

    return render(request,'services/review_service.html',{'massgae':massage})