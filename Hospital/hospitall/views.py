from django.shortcuts import render ,redirect
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpRequest
from django.shortcuts import render
from .models import Clinic, Doctor, Appointment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Clinic
from django.shortcuts import render, redirect, get_object_or_404
from .models import Clinic
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Clinic
from django.shortcuts import render
from .models import Appointment


# Create your views here.

def clinic_detail_view(request, clinic_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    return render(request, 'hospitall/clinic_detail.html', {'clinic': clinic})

def show_clinics(request):
    clinics = Clinic.objects.all()
    return render(request, 'hospitall/clinic.html', {'clinics': clinics})

def show_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospitall/doctor.html', {'doctors': doctors})

from django.contrib.auth.decorators import login_required

@login_required
def show_appointments(request):
    appointments = Appointment.objects.prefetch_related('doctor__clinics').filter(user=request.user)
    return render(request, 'hospitall/Appointment.html', {'appointments': appointments})

# ...

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
        doctors = Doctor.objects.all()  # Corrected variable name
        clinics = Clinic.objects.all()
        return render(request, 'hospitall/create_appointment.html', {'doctors': doctors, 'clinics': clinics})

def is_staff(user):
    return user.is_staff

@user_passes_test(is_staff)
def delete_clinic(request, clinic_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    clinic.delete()
    return redirect('hospitall:show_clinics')
def clinic_view(request, clinic_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    return render(request, 'hospitall/clinic.html', {'clinic': clinic})



@login_required
def create_clinic(request):
    if request.method == "POST":
        clinic_name = request.POST["clinic_name"]
        doctor_user_id = request.POST["doctor_user"]
        doctor_user = User.objects.get(id=doctor_user_id)

        # إنشاء كائن Clinic جديد وحفظه في قاعدة البيانات
        clinic = Clinic(name=clinic_name)
        clinic.save()

        # جلب كائن Doctor الموجود أو إنشاء واحد جديد وحفظه في قاعدة البيانات
        doctor, created = Doctor.objects.get_or_create(user=doctor_user)
        doctor.clinics.add(clinic)

        return redirect('hospitall:show_clinics')
    else:
        doctors = Doctor.objects.all()
        return render(request, 'hospitall/create_clinic.html', {'doctors': doctors})
    
