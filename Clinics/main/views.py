from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic, Review, Contact
from doctors.models import Doctor
# Create your views here.


def home_view(request: HttpRequest):

    return render(request, "main/home.html")


def add_clinic(request: HttpRequest):
    if not request.user.has_perm("clinic.add_clinic"):
        return render(request, 'main/not_authorized.html')

    if request.method == "POST":
        new_clinic = Clinic(name=request.POST["name"], about=request.POST["about"],
                            category=request.POST["category"], image=request.FILES["image"], location=request.POST["location"])
        new_clinic.save()
        return redirect("main:display")

    return render(request, "main/add_clinic.html", {"categories": Clinic.categories})


def display(request: HttpRequest):

    if "category" in request.GET and request.GET["category"] == "Gynecology":
        clinic = Clinic.objects.filter(category__icontains="Gynecology")

    elif "category" in request.GET and request.GET["category"] == "Dentistry":
        clinic = Clinic.objects.filter(category__icontains="Dentistry")

    elif "category" in request.GET and request.GET["category"] == "Pediatric":
        clinic = Clinic.objects.filter(category__icontains="Pediatric")

    elif "category" in request.GET and request.GET["category"] == "Psychiatry":
        clinic = Clinic.objects.filter(category__icontains="Psychiatry")

    elif "category" in request.GET and request.GET["category"] == "Neurology":
        clinic = Clinic.objects.filter(category__icontains="Neurology")

    elif "category" in request.GET and request.GET["category"] == "Dermatology":
        clinic = Clinic.objects.filter(category__icontains="Dermatology")

    else:
        clinic = Clinic.objects.all()

    return render(request, "main/display.html", {"clinics": clinic})


def detail_clinic(request: HttpRequest, clinic_id):

    clinic_detail = Clinic.objects.get(id=clinic_id)
    doctors = Doctor.objects.all()

    if request.method == "POST":
        new_clinic = Review(
            Clinic=clinic_detail, rating=request.POST["rating"], comment=request.POST["comment"])
        new_clinic.save()

    review = Review.objects.filter(Clinic=clinic_detail)

    return render(request, "main/detail.html", {"clinic": clinic_detail, "review": review, "doctors": doctors})


def update_clinic(request: HttpRequest, clinic_id):
    if not request.user.is_staff:
        return render(request, 'main/not_authorized.html')

    clinic = Clinic.objects.get(id=clinic_id)

    if request.method == "POST":
        clinic.name = request.POST["name"]
        clinic.about = request.POST["about"]
        clinic.location = request.POST["location"]
        clinic.category = request.POST["category"]
        clinic.image = request.FILES["image"]
        clinic.save()

        return redirect("main:display")
    return render(request, "main/update_clinic.html", {"clinic": clinic, "categories": Clinic.categories})


def delete_clinic(request: HttpRequest, clinic_id):
    if not request.user.has_perm("clinic.delete_clinic"):
        return render(request, 'main/not_authorized.html')

    clinic = Clinic.objects.get(id=clinic_id)
    clinic.delete()
    return redirect("main:display")


def search(request: HttpRequest):

    if "search" in request.GET:
        keyword = request.GET["search"]
        clinic = Clinic.objects.filter(name__icontains=keyword)
    else:
        clinic = Clinic.objects.all()

    return render(request, "main/search.html", {"clinic": clinic})


def contact(request: HttpRequest):
    if request.method == "POST":
        new_ask = Contact(user_name=request.POST["name"], email=request.POST["email"],
                          message=request.POST["message"])
        new_ask.save()
        return redirect("main:contact")
    return render(request, "main/contact.html")


def client_contact(request: HttpRequest):
    if not request.user.is_staff:
        return render(request, 'main/not_authorized.html')

    Contact.objects.all()
    contact = Contact.objects.all()
    return render(request, "main/client_contact.html", {"contact": contact})


def about_clinic(request: HttpRequest):
    return render(request, "main/about_us.html")


def manage(request: HttpRequest):
    if not request.user.is_staff:
        return render(request, 'main/not_authorized.html')
    return render(request, "main/manage.html")
