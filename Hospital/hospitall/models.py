from django.db import models
from django.contrib.auth.models import User

class Clinic(models.Model):    
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)

    def __str__(self):
         return self.user.username

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} appointment with {self.doctor.user.username} on {self.date}"
