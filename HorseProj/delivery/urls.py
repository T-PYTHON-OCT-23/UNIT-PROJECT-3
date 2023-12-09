from django.urls import path
from . import views

app_name = "delivery"

urlpatterns = [ 
    path('add/', views.add_store_view, name="add_store_view"),
    path('', views.home_store_view, name="home_store_view"),
]