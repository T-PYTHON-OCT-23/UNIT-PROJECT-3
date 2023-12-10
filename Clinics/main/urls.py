from django.urls import path
from . import views
app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("add/", views.add_clinic, name="add_clinic"),
    path("display/", views.display, name="display"),
    path("detail/", views.detail_clinic, name="detail_clinic"),
    path("about/", views.about_clinic, name="about_clinic"),
    path("contact/", views.contact, name="contact"),
]
