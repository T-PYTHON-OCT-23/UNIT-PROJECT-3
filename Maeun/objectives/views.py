from django.shortcuts import render ,redirect
from django.http import HttpRequest , HttpResponse
from .models import Objective

# Create your views here.

def show_objectives(request:HttpRequest):
    objs = Objective.objects.all()
    obj_count=objs.count()
    
    return render(request, "objectives/show_objectives.html",{"objs":objs, "obj_count" : obj_count})

def add_view(request:HttpRequest):
    
    
    msg=None
    if request.method == "POST":
        try:
            new_obj = Objective(name=request.POST["name"],description=request.POST["description"], category=request.POST["category"]) 
            if "poster" in request.FILES:
                new_obj.poster = request.FILES["poster"]

            new_obj.save()
            return redirect("main:home_view")
        except Exception as e:
            msg = f"An error occured, please fill in all fields and try again . {e}"

            
    return render(request,"objectives/add.html",{"categories" : Objective.categories,  "msg" : msg})

def my_objectives_view(request:HttpRequest):
    objs = Objective.objects.all()
    obj_count=objs.count()
    
    return render(request, "objectives/my_objectives.html",{"objs":objs , "obj_count" : obj_count})

def delete_objective_view(request:HttpRequest, obj_id):
    
    obj = Objective.objects.get(id=obj_id)
    obj.delete()
    return redirect("objectives:my_objectives_view")

def update_objective_view(request: HttpRequest, obj_id):

    
    obj = Objective.objects.get(id=obj_id)

    if request.method == "POST":
        obj.name = request.POST["name"]
        obj.description = request.POST["description"]
        obj.category = request.POST["category"]
        obj.save()

        return redirect('objectives:my_objectives_view', obj_id=obj_id)

    return render(request, "objectives/update.html", {"obj" : obj, "categories"  : Objective.categories})
