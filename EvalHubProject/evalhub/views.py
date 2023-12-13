from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from .models import CustomUser, Task, Feedback
from django.contrib.auth.models import User
from django.db import IntegrityError

def register_user_view(request: HttpRequest):
    msg = None
    if request.method == "POST":
        user: User = User.objects.create_user(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
        user.save()

        c_user: CustomUser= CustomUser(user=user)
        c_user.save()
        return redirect("evalhub:login_user_view")

    return render(request, 'evalhub/register.html', {"msg" : msg}) 

def login_user_view(request: HttpRequest):
    msg = None
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            login(request, user)
            return redirect("evalhub:home_page_view")
        else:
            msg = "Please provide correct username and password"

    return render(request, 'evalhub/login.html', {"msg" : msg}) 

def logout_user_view(request: HttpRequest):
    logout(request)
    return redirect('evalhub:login_user_view')  


def user_profile_view(request: HttpRequest, user_id):
    user = request.user

    return render(request, 'evalhub/user_profile.html', {'user': user})  

def update_user_view(request: HttpRequest):
    msg = None

    if request.method == "POST":
        try:
            if request.user.is_authenticated:
                user : User = request.user
                user.first_name = request.POST["first_name"]
                user.last_name = request.POST["last_name"]
                user.email = request.POST["email"]
                user.save()

                return redirect("evalhub:user_profile_view", user_id = request.user.id)

            else:
                return redirect("accounts:login_user_view")
        except IntegrityError as e:
            msg = f"Please select another username"
        except Exception as e:
            msg = f"something went wrong {e}"

    return render(request, 'evalhub/update_user.html', {"msg" : msg})  

def home_page_view(request: HttpRequest):

    return render(request, 'evalhub/home_page.html')

def add_task_view(request: HttpRequest):
    msg = None
    employees=CustomUser.objects.filter(manager=request.user)

    if request.method == "POST":
        try:
            new_task = Task(title=request.POST["title"], manager=request.user, employee= User.objects.get(username=request.POST["employee"]), description=request.POST["description"], due_date=request.POST["due_date"]) 
            new_task.save()
            return redirect("evalhub:task_list")
        except Exception as e:
            msg = f"An error occured, please fill in all fields and try again . {e}"

    return render(request, "evalhub/add_task.html", {"status_choices" : Task.status_choices ,  "msg" : msg, "employees":employees})

def task_list(request: HttpRequest):

    as_m_tasks: Task = Task.objects.filter(employee=request.user)
    as_e_tasks: Task = Task.objects.filter(manager=request.user)

    return render(request, 'evalhub/task_list.html', {'as_e_tasks': as_e_tasks , 'as_m_tasks': as_m_tasks})  

def task_detail(request: HttpRequest, task_id):
    task: Task = get_object_or_404(Task, id=task_id)
    return render(request, 'evalhub/task_detail.html', {'task': task})  

def feedback_detail(request: HttpRequest, task_id):
    task: Task = get_object_or_404(Task, pk=task_id, manager=request.user.customuser)
    feedback: False = Feedback.objects.get(task=task)
    return render(request, 'evalhub/feedback_detail.html', {'feedback': feedback})  

def complete_task(request: HttpRequest, task_id):
    task = get_object_or_404(Task, pk=task_id, manager=request.user.customuser)

    if task.completed:
        messages.error(request, 'Task is already completed.')
        return redirect('task_list')  

    task.completed = True
    task.save()


    messages.success(request, 'Task completed successfully.')
    return redirect('task_list')  
