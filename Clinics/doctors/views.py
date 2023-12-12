from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Doctor
from main.models import Clinic

# Create your views here.


def doctor_home(request: HttpRequest):
    doctor = Doctor.objects.all()
    return render(request, "doctors/doctor_home.html", {"doctors": doctor})


def add_doctor(request: HttpRequest):
    if not request.user.has_perm("doctor.add_doctor"):
        return render(request, 'main/not_authorized.html')

    if request.method == "POST":
        new_doctor = Doctor(name=request.POST["name"], bio=request.POST["bio"], avatar=request.FILES.get(
            "avatar", "image/avatar.jpg"))
        new_doctor.save()
        return redirect("doctors:doctor_home")

    return render(request, "doctors/add_doctor.html")


def add_clinic_doctor(request: HttpRequest, clinic_id, doctor_id):
    if not request.user.has_perm("doctor.add_doctor"):
        return render(request, 'main/not_authorized.html')

    clinic = Clinic.objects.get(id=clinic_id)
    doctors = Doctor.objects.get(id=doctor_id)
    clinic.doctors.add(doctors)

    return redirect("main:detail_clinic", clinic_id=clinic_id)


def doctor_detail(request: HttpRequest, doctor_id):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except:
        return render(request, "main/not_found.html")
    return render(request, "doctors/doctor_detail.html", {"doctor": doctor})


def remove_clinic_doctor(request: HttpRequest, clinic_id, doctor_id):

    if not request.user.has_perm("doctor.delete_doctor"):
        return render(request, "main/not_authorized.html")

    clinic = Clinic.objects.get(id=clinic_id)
    doctors = Doctor.objects.get(id=doctor_id)
    clinic.doctors.remove(doctors)

    return redirect("main:detail_clinic", clinic_id=clinic_id)
