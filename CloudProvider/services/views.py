from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Service, ServiceDetails
# Create your views here.

# this for admin to add new service 
def add_service_view(request:HttpRequest):
    massage = ''
    #check here if he a staff 
    #if request.user.is_authenticated:
    if request.method == 'POST':
        try:
            new_services = Service(service_name=request.POST['service_name'],description=request.POST['description'],type=request.POST['type'],image=request.FILES['image'],price=request.POST['price'])
            new_services.save()
            return redirect('services:show_services_view')
        except Exception as e:
            massage = f"something went wrong{e}"

    return render(request,'services/add_services.html',{"massage":massage,"service_name":Service.types,"pricese":Service.pricese})

# fro user in home 
def show_services_view(request:HttpRequest):
    massage = ''
    # check if the user login
    try:
        service = Service.objects.all()
    except Exception as e:
        massage = f"Something went wrong {e}"

    return render(request,'services/show_services.html',{"massage":massage,"services":service})

# this for admin to edit new service 
def edit_service_view(request:HttpRequest,service_id):
    massage = ''
    try:
        request_edit = ServiceDetails.objects.get(id=service_id)
    except Exception as e:
        massage = f'{e}'
    return render(request,'services/review_service_request.html',{"massage":massage,'show':request_edit})

# this is for both admin and user, admin can review the service and user can review his own service
def review_service_view(request:HttpRequest):
    massage = ''

    return render(request,'services/review_service.html',{"massage":massage})

# for user to see more spacefication about the service 
def service_detils_view(request:HttpRequest,service_id):
    massage = ''
    try:
        service = Service.objects.get(id=service_id)
    except Exception as e:
        massage = f'{e}'

    return render(request,'services/service_detils.html',{'massgae':massage,'service':service})

#Need for test tomorrow
def request_service_view(request:HttpRequest,serivce_id):
    massage = ''
    # if the method POST add new_Request
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                new_service = Service.objects.get(id=serivce_id)
                user = User.objects.get(id=request.user.id)
                new_Request_detils = ServiceDetails(user=user,service=new_service,private_endpoint=request.POST['private_endpoint'],public_endpoint=request.POST['public_endpoint'],private_ip=request.POST['private_ip'],public_ip=request.POST['public_ip'],elastic_ip=request.POST['elastic_ip'],platfrom=request.POST['platfrom'],life_cycle=request.POST['life_cycle'],high_availability=request.POST['high_availability'])
                new_Request_detils.save()

                return redirect('services:view_services_i_reqeust_view')
            except Exception as e:
                massage = f"something went wrong {e}"
    
    try:
        service = Service.objects.get(id=serivce_id)
    except Exception as e:
        massage = f'{e}'

    return render(request,'services/request_service.html',{'service':service,'massage':massage,'service_request':ServiceDetails})

#Need for testing tomorrow
def view_services_i_reqeust_view(request:HttpRequest):
    massage = ''
    if request.user.is_authenticated:
        try:
            show_services = ServiceDetails.objects.filter(user=request.user.id,status='pending')#here i add service = service_id so i can supporate

        except Exception as e:
            massage = f'something went wrong "{e}"'
    else:
        return redirect('user:login_view')
    
    return render(request,'services/view_services_i_request.html',{'massage':massage,'show_serivces':show_services})


def delete_reqeust_view(request:HttpRequest,request_id):
    try:
        request_edit = ServiceDetails.objects.get(id=request_id)
        request_edit.delete()
        return redirect('services:view_services_i_reqeust_view')
    except Exception as e:
        massage = f'{e}'


def edit_request_view(reqeust:HttpRequest,request_id):
    massage = ''
    try:
        request_edit = ServiceDetails.objects.get(id=request_id)
    except Exception as e:
        massage = f'{e}'
    
    if reqeust.method == 'POST':
        try:
            new_edit_reqeust = ServiceDetails.objects.get(id=request_id)
            new_edit_reqeust.private_endpoint = reqeust.POST['private_endpoint']
            new_edit_reqeust.public_endpoint = reqeust.POST['public_endpoint']
            new_edit_reqeust.private_ip = reqeust.POST['private_ip']
            new_edit_reqeust.public_ip = reqeust.POST['public_ip']
            new_edit_reqeust.elastic_ip = reqeust.POST['elastic_ip']
            new_edit_reqeust.platfrom = reqeust.POST['platfrom']
            new_edit_reqeust.life_cycle = reqeust.POST['life_cycle']
            new_edit_reqeust.high_availability = reqeust.POST['high_availability']
            new_edit_reqeust.save()
            return redirect('services:edit_request_view',request_id=new_edit_reqeust.id)
        except Exception as e:
            massage = f'{e}'

    return render(reqeust,'services/edit_request.html',{'service_request':request_edit,'massage':massage})


def delete_service_view(request:HttpRequest):
    massage = ''
    try:
        services = Service.objects.all()
    except Exception as e:
        massage = f'{e}'

    return render(request,'services/delete_service.html',{'services':services,'massage':massage})

def delete_service_now_view(request:HttpRequest,service_id):
    massage = ''
    try:
        services = Service.objects.get(id=service_id)
        services.delete()
        return redirect('services:show_services_view')
    except Exception as e:
        massage = f'{e}'
    return