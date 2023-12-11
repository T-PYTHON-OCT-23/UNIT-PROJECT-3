from django.urls import path
from . import views
app_name = "services"

urlpatterns = [
    path("add/services", views.addServices, name="addServices"),
    path("view/services", views.viewServices, name="viewServices"),
    path("details/<service_id>/", views.serviceDetails, name="serviceDetails"),
    path("update/<service_id>/", views.updateService, name="updateService"),
    path("delete/<service_id>/", views.deleteService, name="deleteService"),
    path("search/", views.searchService, name="searchService"),
]