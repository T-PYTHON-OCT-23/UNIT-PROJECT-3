from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from .models import CustomUser, Task, Feedback, Report
from django.contrib.auth.models import User
from django.db import IntegrityError

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

def add_report_view(request: HttpRequest, task_id):
    msg = None
    task=Task.objects.get(id=task_id)
    if request.method == "POST":
        try:
            new_report : Report = Report(task=task, submitted_by=request.user, report_text=request.POST["report_text"], submitted_to=task.manager) 
            new_report.save()
            return redirect("evalhub:report_list")
        except Exception as e:
            msg = f"An error occured, please fill in all fields and try again . {e}"

    return render(request, "evalhub/add_report.html", {"msg" : msg,"task":task})

def task_list(request: HttpRequest):
    
    as_m_tasks: Task = Task.objects.filter(employee=request.user)
    as_e_tasks: Task = Task.objects.filter(manager=request.user)

    return render(request, 'evalhub/task_list.html', {'as_e_tasks': as_e_tasks , 'as_m_tasks': as_m_tasks})  

def report_list(request: HttpRequest ):
    report_as_e=Report.objects.filter(submitted_to=request.user)
    report_as_m=Report.objects.filter(submitted_by=request.user)

    return render(request, 'evalhub/report_list.html', {'report_as_e':report_as_e, 'report_as_m':report_as_m})  

def task_detail(request: HttpRequest, task_id):
    task: Task = get_object_or_404(Task, id=task_id)
    return render(request, 'evalhub/task_detail.html', {'task': task})  

def report_detail(request: HttpRequest, report_id):
    report: Report = get_object_or_404(Report, id=report_id)
    return render(request, 'evalhub/report_detail.html', {'report': report})

def feedback_detail(request: HttpRequest, task_id):
    task: Task = get_object_or_404(Task, id=task_id)
    feedback = Feedback.objects.get(task=task)
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
