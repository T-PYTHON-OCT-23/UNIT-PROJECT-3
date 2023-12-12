from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("riyadhExpo/", views.riyadh_expo_view, name="riyadh_expo_view"),
    


]