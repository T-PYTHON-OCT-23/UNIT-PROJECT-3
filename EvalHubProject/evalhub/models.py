from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user") 
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="manager")
    performance_rating = models.FloatField(null=True, blank=True)
    about = models.TextField(default="",null=True, blank=True,)
    birth_date = models.DateField(null=True , blank=True)
    avatar = models.ImageField(upload_to="images/", default="images/avatar-default.png")

    def __str__(self):
        return self.user.username

class Task(models.Model):

    status_choices = models.TextChoices("task_status", ["Done", "Late", "Progress", "Pending", "Canceled"])

    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_assigned')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_required')
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=64, choices=status_choices.choices, default="Pending")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Report(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='reports')
    report_text = models.TextField()
    submitted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reports_submitted')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for Task: {self.task.title}"

class Feedback(models.Model):
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='feedback')
    notes = models.TextField()
    completion_status = models.BooleanField(default=False)
    due_date_extension = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Feedback for Task: {self.task.title}"