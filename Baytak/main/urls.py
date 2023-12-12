from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.homePage, name="homePage"),
    path("contact/us", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("thank", views.thank, name="thank"),
    path("disaplay/contact/", views.displayContact, name="allContact"),
]