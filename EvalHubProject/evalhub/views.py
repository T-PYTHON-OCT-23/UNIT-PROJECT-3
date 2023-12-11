from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser, Task, Feedback

def register_user_view(request):
    if request.method == 'POST':
        # Handle user registration logic here
        # Example: create a new CustomUser instance and save it
        # Redirect to login_user_view or any other desired page
        pass
    return render(request, 'evalhub/register.html')  # Replace 'registration/register.html' with your registration template path

def login_user_view(request):
    if request.method == 'POST':
        # Handle user login logic here
        # Example: use authenticate() and login() functions
        pass
    return render(request, 'evalhub/login.html')  # Replace 'registration/login.html' with your login template path

@login_required
def logout_user_view(request):
    logout(request)
    return redirect('login_user_view')  # Replace 'login_user_view' with your login view name or URL

@login_required
def user_profile_view(request):
    user = request.user
    # Retrieve and display user profile information
    return render(request, 'evalhub/user_profile.html', {'user': user})  # Replace 'user_profile.html' with your user profile template path

@login_required
def update_user_view(request):
    user = request.user
    if request.method == 'POST':
        # Handle user profile update logic here
        # Example: update user information and save changes
        pass
    return render(request, 'evalhub/update_user.html', {'user': user})  # Replace 'update_user.html' with your update user template path

@login_required
def task_list(request):
    tasks = Task.objects.filter(manager=request.user.customuser)
    return render(request, 'evalhub/task_list.html', {'tasks': tasks})  # Replace 'task_list.html' with your task list template path

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id, manager=request.user.customuser)
    return render(request, 'evalhub/task_detail.html', {'task': task})  # Replace 'task_detail.html' with your task detail template path

@login_required
def feedback_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id, manager=request.user.customuser)
    feedback = Feedback.objects.get(task=task)
    return render(request, 'evalhub/feedback_detail.html', {'feedback': feedback})  # Replace 'feedback_detail.html' with your feedback detail template path

@login_required
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
