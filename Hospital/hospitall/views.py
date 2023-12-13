from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpRequest
from .models import Clinic, Doctor, Appointment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.mail import send_mail

def clinic_detail_view(request, clinic_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    info = ""
    if clinic.name == "Dental clinic":  # check the clinic name
        info = "A dental clinic is where people go to get specialized medical care for their oral health. Dentists can diagnose and treat a wide range of conditions, including tooth decay, gum disease, and orthodontic problems."
    elif clinic.name == "Ear and throat clinic":
        info = "An ear, nose and throat clinic is where people with ear, nose and throat problems go. Otolaryngologists can diagnose and treat a wide range of these conditions, including ear infections, sinusitis, sore throat, tinnitus, hearing loss, swallowing problems, and cancer of the ear, nose, and throat."
    elif clinic.name == "family Medicine":
        info = "A family medicine clinic is where people go to get comprehensive primary health care. Family doctors can diagnose and treat a wide range of conditions, including common diseases, chronic diseases and serious diseases."
    elif clinic.name == "Internal Medicine Clinic":
        info = "An internal medicine clinic is where people go to get specialized medical care for diseases that affect the internal organs of the body. Internists can diagnose and treat a wide range of these conditions, including cardiovascular disease, respiratory disease, kidney disease, liver disease, and gastrointestinal disease."
    elif clinic.name == "Orthopedic Clinic":
        info = "An orthopedic clinic is where people go who have problems with their bones, joints and muscles. Orthopedists can diagnose and treat a wide range of these conditions, including fractures, arthritis, and bone deformities."
    return render(request, 'hospitall/clinic_detail.html', {'clinic': clinic, 'info': info})

def show_clinics(request):
    clinics = Clinic.objects.all()
    return render(request, 'hospitall/clinic.html', {'clinics': clinics})

def show_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospitall/doctor.html', {'doctors': doctors})

@login_required
def show_appointments(request):
    appointments = Appointment.objects.prefetch_related('doctor__clinics').filter(user=request.user)
    return render(request, 'hospitall/Appointment.html', {'appointments': appointments})

@login_required
def create_appointment(request):
    if request.method == "POST":
        clinic_id = request.POST["clinic"]
        clinic = Clinic.objects.get(id=clinic_id)
        date = request.POST["date"]

        doctor = Doctor.objects.filter(clinics=clinic).first()

        if doctor is not None:
            appointment = Appointment(user=request.user, doctor=doctor, clinic=clinic, date=date)
            appointment.save()

            if "sendEmail" in request.POST:
                send_mail(
                    'Appointment Confirmation',
                    f'You have an appointment with {doctor.user.username} at {clinic.name} on {date}.',
                    'your-email@example.com',  # replace with your email
                    [request.user.email],
                    fail_silently=False,
                )

            return redirect('hospitall:show_appointments')
        else:
            return render(request, 'hospitall/create_appointment.html', {'error': 'No doctor found for the selected clinic.'})
    else:
        clinics = Clinic.objects.all()
        return render(request, 'hospitall/create_appointment.html', {'clinics': clinics})

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
        clinic_image = request.FILES["clinic_image"]  
        doctor_user_id = request.POST["doctor_user"]
        doctor_user = User.objects.get(id=doctor_user_id)
        clinic = Clinic(name=clinic_name, image=clinic_image)  
        clinic.save()
        doctor, created = Doctor.objects.get_or_create(user=doctor_user)
        doctor.clinics.add(clinic)

        return redirect('hospitall:show_clinics')
    else:
        doctors = Doctor.objects.all()
        return render(request, 'hospitall/create_clinic.html', {'doctors': doctors})

@login_required
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.user == appointment.user:
        appointment.delete()
    return redirect('hospitall:show_appointments')
