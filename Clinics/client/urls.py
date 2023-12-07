from django.urls import path
from . import views
app_name = "client"
urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("profile/<user_id>/", views.user_profile, name="user_profile"),
    path("update/", views.update_user, name="update_user")
]