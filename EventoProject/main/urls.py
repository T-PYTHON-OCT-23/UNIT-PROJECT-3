from django.urls import path
from . import views
app_name = "main"


urlpatterns = [
    path("", views.home_page_view, name="home_page_view"),
    path("contact_us/", views.contact_us_view , name="contact_us_view"),
    path("about_us/", views.about_us_view, name="about_us_view")

]
