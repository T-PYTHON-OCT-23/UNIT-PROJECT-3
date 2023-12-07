from django.urls import path
from . import views
app_name = "events"


urlpatterns = [
    path("add/", views.add_event_view, name="add_event_view"),
    path("", views.event_home_view, name="event_home_view"),
    path("delete/<event_id>", views.delete_event_view, name="delete_event_view"),
    path("detail/<event_id>/", views.event_detail_view, name="event_detail_view"),

]
