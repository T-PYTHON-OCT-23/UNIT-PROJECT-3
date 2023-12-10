from django.urls import path
from . import views
app_name = "request"

urlpatterns = [
    path('<service_id>/add/', views.addRequest, name="addRequest"),
    path('', views.veiwRequest, name="veiwRequest")
    
    
]