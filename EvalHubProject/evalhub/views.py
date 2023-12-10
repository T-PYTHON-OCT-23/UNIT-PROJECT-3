# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, Report, Feedback
from .forms import ReportForm, FeedbackForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(manager=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    report_form = ReportForm()

    if request.method == 'POST':
        report_form = ReportForm(request.POST)
        if report_form.is_valid():
            report = report_form.save(commit=False)
            report.task = task
            report.submitted_by = request.user
            report.save()
            return redirect('task_detail', task_id=task.id)

    return render(request, 'task_detail.html', {'task': task, 'report_form': report_form})

@login_required
def feedback_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    feedback_form = FeedbackForm()

    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback = feedback_form.save(commit=False)
            feedback.manager = request.user
            feedback.task = task
            feedback.save()
            return redirect('task_detail', task_id=task.id)

    return render(request, 'feedback_detail.html', {'task': task, 'feedback_form': feedback_form})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')
