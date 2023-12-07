from django.urls import path
from . import views

app_name = "objectives"

urlpatterns = [
    path("add/",views.add_view, name="add_view")
    
]