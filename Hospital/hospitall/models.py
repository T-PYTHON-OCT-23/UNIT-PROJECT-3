from django.db import models
from django.contrib.auth.models import User

class Clinic(models.Model):    
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='clinics/', default='images/default.jpg')  # new field
    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clinics = models.ManyToManyField(Clinic)


    def __str__(self):
         return self.user.username

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)  # New field
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} appointment with {self.doctor.user.username} at {self.clinic.name} on {self.date}"
