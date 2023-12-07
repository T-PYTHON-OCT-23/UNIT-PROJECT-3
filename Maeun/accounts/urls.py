from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.register_user_view, name="register_user_view"),
    
]