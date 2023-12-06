from django.urls import path
from . import views

app_name="hospitall"

urlpatterns = [
    path('', views.show_clinics, name='show_clinics'),
    path('doctors/', views.show_doctors, name='show_doctors'),
    path('appointments/', views.show_appointments, name='show_appointments'),
    path('create_appointment/', views.create_appointment, name='create_appointment'),
    path('clinic/<int:clinic_id>/',views.clinic_detail_view, name='clinic_detail_view'),


    path('create_appointment/<int:doctor_id>/',views.create_appointment, name='create_appointment'),

]