from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    role = models.CharField(max_length=20, choices=[("manager", "Manager"), ("employee", "Employee")])
    pfp = models.ImageField(upload_to="images/", default="images/avatar-default.png")

    def __str__(self):
        return self.user.username

class Task(models.Model):
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks_assigned')
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks_required')
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
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
    
