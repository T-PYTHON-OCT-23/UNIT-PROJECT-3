from django.urls import path
from . import views

app_name = "doctors"

urlpatterns = [
    path("add/", views.add_doctor, name="add_doctor"),
    path("", views.doctor_home, name="doctor_home"),
    path("add/<clinic_id>/<doctor_id>/", views.add_clinic_doctor, name="add_clinic_doctor"),
    path("remove/<clinic_id>/<doctor_id>/", views.remove_clinic_doctor, name="remove_clinic_doctor"),
    path("doctor/<doctor_id>/", views.doctor_detail, name="doctor_detail")
]