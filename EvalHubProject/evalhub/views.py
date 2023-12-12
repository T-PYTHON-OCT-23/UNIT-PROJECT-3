from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser, Task, Feedback
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

def register_user_view(request):
    msg = None

    if request.method == "POST":
        try:
            #create a new user
            user = User.objects.create_user(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
            user.save()

            return redirect("accounts:login_user_view")
        except IntegrityError as e:
            msg = f"Please select another username"
        except Exception as e:
            msg = f"something went wrong {e}"

    return render(request, "accounts/register.html", {"msg" : msg})
    return render(request, 'evalhub/register.html')  # Replace 'registration/register.html' with your registration template path

def login_user_view(request):
    if request.method == 'POST':
        # Handle user login logic here
        # Example: use authenticate() and login() functions
        pass
    return render(request, 'evalhub/login.html')  # Replace 'registration/login.html' with your login template path


def logout_user_view(request):
    logout(request)
    return redirect('login_user_view')  # Replace 'login_user_view' with your login view name or URL

def user_profile_view(request):
    user = request.user
    # Retrieve and display user profile information
    return render(request, 'evalhub/user_profile.html', {'user': user})  # Replace 'user_profile.html' with your user profile template path

def update_user_view(request):
    user = request.user
    if request.method == 'POST':
        # Handle user profile update logic here
        # Example: update user information and save changes
        pass
    return render(request, 'evalhub/update_user.html', {'user': user})  # Replace 'update_user.html' with your update user template path

def home_page_view(request):

    return render(request, 'evalhub/home_page.html')

def task_list(request):
    tasks: Task = Task.objects.filter(manager=request.user.customuser)
    return render(request, 'evalhub/task_list.html', {'tasks': tasks})  # Replace 'task_list.html' with your task list template path

def task_detail(request, task_id):
    task: Task = get_object_or_404(Task, pk=task_id, manager=request.user.customuser)
    return render(request, 'evalhub/task_detail.html', {'task': task})  # Replace 'task_detail.html' with your task detail template path

def feedback_detail(request, task_id):
    task: Task = get_object_or_404(Task, pk=task_id, manager=request.user.customuser)
    feedback: False = Feedback.objects.get(task=task)
    return render(request, 'evalhub/feedback_detail.html', {'feedback': feedback})  # Replace 'feedback_detail.html' with your feedback detail template path

def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, manager=request.user.customuser)

    # Check if the task is already completed
    if task.completed:
        messages.error(request, 'Task is already completed.')
        return redirect('task_list')  # Replace 'task_list' with your task list view name or URL

    # Mark the task as completed
    task.completed = True
    task.save()

    # Add any additional logic you need for task completion

    messages.success(request, 'Task completed successfully.')
    return redirect('task_list')  # Replace 'task_list' with your task list view name or URL
