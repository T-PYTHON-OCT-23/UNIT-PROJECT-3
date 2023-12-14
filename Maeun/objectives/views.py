from django.shortcuts import render ,redirect
from django.http import HttpRequest , HttpResponse
from .models import Objective , Order
from accounts.models import Profile
import datetime

# Create your views here.

def show_objectives(request:HttpRequest):
    objs = Objective.objects.all()
    obj_count=objs.count()
    
    if "filter" in request.GET and request.GET["filter"]=="Equipment":
        objs = Objective.objects.filter(category="Equipment")
    if "filter" in request.GET and request.GET["filter"]=="Houseware":
        objs = Objective.objects.filter(category="Houseware")
    if "filter" in request.GET and request.GET["filter"]=="Agriculture tools":
        objs = Objective.objects.filter(category="Agriculture tools")
    if "filter" in request.GET and request.GET["filter"]=="Car tools":
        objs = Objective.objects.filter(category="Car tools")  
    if "filter" in request.GET and request.GET["filter"]=="Other":
        objs = Objective.objects.filter(category="Other")  
    
    if "search" in request.GET:
        search = request.GET["search"]
        objs = Objective.objects.filter(name__contains=search)
    return render(request, "objectives/show_objectives.html",{"objs":objs, "obj_count" : obj_count})

def add_view(request:HttpRequest):
    
    if not request.user.is_active:
        return render(request, 'main/not_authorized.html' , status=401)
    
    msg=None
    if request.method == "POST":
        try:
            new_obj = Objective(name=request.POST["name"],description=request.POST["description"], category=request.POST["category"],user=request.user) 
            if "poster" in request.FILES:
                new_obj.poster = request.FILES["poster"]

            new_obj.save()
            return redirect("objectives:my_objectives_view")
        except Exception as e:
            msg = f"An error occured, please fill in all fields and try again . {e}"

            
    return render(request,"objectives/add.html",{"categories" : Objective.categories,  "msg" : msg})

def my_objectives_view(request:HttpRequest):
    if not request.user.is_active:
        return render(request, 'main/not_authorized.html' , status=401)
    objs = Objective.objects.filter(user=request.user)
    obj_count=objs.count()
    
    return render(request, "objectives/my_objectives.html",{"objs":objs , "obj_count" : obj_count})

def delete_objective_view(request:HttpRequest, obj_id):
    if not request.user.is_active:
        return render(request, 'main/not_authorized.html' , status=401)
    obj = Objective.objects.get(id=obj_id)
    obj.delete()
    
    return redirect("objectives:my_objectives_view")

def update_objective_view(request: HttpRequest, obj_id):
    if not request.user.is_active:
        return render(request, 'main/not_authorized.html' , status=401)
    msg=None
    obj = Objective.objects.get(id=obj_id)
    try:
        if request.method == "POST":
            obj.name = request.POST["name"]
            obj.description = request.POST["description"]
            obj.category = request.POST["category"]
            obj.reserved=request.POST["reserved"]
            obj.save()
        return redirect('objectives:my_objectives_view')
    except Exception as e :
        msg = f"An error occured, please fill in all fields and try again . {e}"


    return render(request, "objectives/update.html", {"obj" : obj, "categories"  : Objective.categories,"msg":msg})

def my_objectives_borrowed_view(request:HttpRequest):
    if not request.user.is_active:
        return render(request, 'main/not_authorized.html' , status=401)
    objs = Objective.objects.filter(user=request.user)
    obj_count=objs.count()
    
    return render(request, "objectives/borrowed.html",{"objs":objs , "obj_count" : obj_count})

def objective_retrieved_view(request:HttpRequest,obj_id):
    if not request.user.is_active:
        return render(request, 'main/not_authorized.html' , status=401)
    obj = Objective.objects.get(id=obj_id)
    obj.reserved = False
    obj.save()

    return redirect("objectives:my_objectives_borrowed_view")
    
def objective_order_view(request:HttpRequest,obj_id):
    if not request.user.is_active:
        return render(request, 'main/not_authorized.html' , status=401)
    obj = Objective.objects.get(id =obj_id)
    msg=None
    try:
        
        if request.method == "POST" :

            new_order = Order(user=request.user, objective=obj,day=request.POST["day"],hour=request.POST["hour"],)
            
            obj.reserved = True
            obj.save()
            
            new_order.save()
            return redirect("objectives:my_order_view")
    except Exception as e :
        msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request,"objectives/order.html",{"obj":obj,"msg":msg})

def my_order_view(request:HttpRequest):
    if not request.user.is_active:
        return render(request, 'main/not_authorized.html' , status=401)
    orders = Order.objects.filter(user=request.user,acceptance=False)
    
    return render(request,"objectives/my_order.html",{"orders":orders})
    
def loan_requests_view(request:HttpRequest):
    if not request.user.is_active:
        return render(request, 'main/not_authorized.html' , status=401)
    orders = Order.objects.filter(objective__user=request.user, acceptance = False)
    
    return render(request,"objectives/loan_requests.html",{"orders":orders})

def order_acceptance_view(request:HttpRequest,order_id):
    if not request.user.is_active:
        return render(request, 'main/not_authorized.html' , status=401)
    order = Order.objects.get(id=order_id)
    order.acceptance = True
    order.save()

    return redirect("objectives:loan_requests_view")

def order_rejection_view(request:HttpRequest,order_id):
    if not request.user.is_active:
        return render(request, 'main/not_authorized.html' , status=401)
    order = Order.objects.get(id=order_id)
    order.objective.reserved = False
    order.objective.save()
    order.delete()

    return redirect("objectives:loan_requests_view")

def borrowed_objectives_view(request:HttpRequest):
    if not request.user.is_active:
        return render(request, 'main/not_authorized.html' , status=401)
    orders = Order.objects.filter(user=request.user,acceptance=True,objective__reserved=True)
    time_now = datetime.datetime.now()
    
    return render(request,"objectives/borrowed_objectives.html",{"orders":orders,"time_now":time_now})
    
    
