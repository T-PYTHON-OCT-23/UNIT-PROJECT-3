from django.shortcuts import render ,redirect
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpRequest
from django.shortcuts import render
from .models import Clinic, Doctor, Appointment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Clinic

# Create your views here.

def show_clinics(request):
    clinics = Clinic.objects.all()
    return render(request, 'hospitall/clinic.html', {'clinics': clinics})

def show_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospitall/doctor.html', {'doctors': doctors})

from django.contrib.auth.decorators import login_required

@login_required
def show_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'hospitall/Appointment.html', {'appointments': appointments})


@login_required
def create_appointment(request):
    if request.method == "POST":
        doctor_id = request.POST["doctor"]
        doctor = Doctor.objects.get(id=doctor_id)
        date = request.POST["date"]
        appointment = Appointment(user=request.user, doctor=doctor, date=date)
        appointment.save()
        return redirect('hospitall:show_appointments')
    else:
        doctors = Doctor.objects.all()
        return render(request, 'hospitall/create_appointment.html', {'doctors': doctors})
    
def clinic_detail_view(request, clinic_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    return render(request, 'hospitall/clinic_detail.html', {'clinic': clinic})