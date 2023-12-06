from django.urls import path
from . import views
from django.urls import path
from .views import delete_clinic

app_name="hospitall"

urlpatterns = [
    path('', views.show_clinics, name='show_clinics'),
    path('doctors/', views.show_doctors, name='show_doctors'),
    path('appointments/', views.show_appointments, name='show_appointments'),
    path('create_appointment/', views.create_appointment, name='create_appointment'),
    path('clinic/<int:clinic_id>/',views.clinic_detail_view, name='clinic_detail_view'),

    path('delete_clinic/<int:clinic_id>/',views.delete_clinic, name='delete_clinic'),

    path('create_appointment/<int:doctor_id>/',views.create_appointment, name='create_appointment'),

    path('delete_clinic/<int:clinic_id>/', views.delete_clinic, name='delete_clinic'),
]

