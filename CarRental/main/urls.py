from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("about/",views.about_page_view,name="about_page_view"),
    path("contact/",views.contact_page_view,name="contact_page_view"),
]