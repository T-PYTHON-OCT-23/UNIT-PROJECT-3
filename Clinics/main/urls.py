from django.urls import path
from . import views
app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("add/", views.add_clinic, name="add_clinic"),
    path("display/", views.display, name="display"),
    path("detail/<clinic_id>/", views.detail_clinic, name="detail_clinic"),
    path("update/<clinic_id>/", views.update_clinic, name="update_clinic"),
    path("delete/<clinic_id>/", views.delete_clinic, name="delete_clinic"),
    path("search/", views.search, name="search"),
    path("about/", views.about_clinic, name="about_clinic"),
    path("contact/", views.contact, name="contact"),
    path("manage/", views.manage, name="manage"),
    path("client/", views.client_contact, name="client_contact"),
]
