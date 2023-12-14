from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("add/register/", views.register_user_view, name="register_user_view"),
    path("login/",views.login_view,name="login_view"),
    path("logout/", views.logout_user_view, name="logout_user_view"),

    
]