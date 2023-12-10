from django.db import models
from django.contrib.auth.models import AbstractUser

class Manager(AbstractUser):
    groups = models.ManyToManyField("auth.Group", related_name="manager_set", blank=True)
    user_permissions = models.ManyToManyField("auth.Permission", related_name="manager_set", blank=True)


    def __str__(self):
        return self.username

class Employee(AbstractUser):

    groups = models.ManyToManyField("auth.Group", related_name="employee_set", blank=True)
    user_permissions = models.ManyToManyField("auth.Permission", related_name="employee_set", blank=True)

    def __str__(self):
        return self.username

class Task(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='tasks_assigned')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='tasks_required')
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Report(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='reports')
    report_text = models.TextField()
    submitted_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reports_submitted')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for Task: {self.task.title}"

class Feedback(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='feedback')
    notes = models.TextField()
    completion_status = models.BooleanField(default=False)
    due_date_extension = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Feedback for Task: {self.task.title}"
    
