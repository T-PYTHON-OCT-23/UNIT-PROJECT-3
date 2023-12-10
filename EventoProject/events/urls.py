from django.urls import path
from . import views
app_name = "events"


urlpatterns = [

    path("", views.events_home_view, name="events_home_view"),
    path("add/", views.add_event_view, name="add_event_view"),
    path("art/", views.art_events_view, name="art_events_view"),
    path("technology/", views.tech_events_view, name="Tech_events_view"),
    path("entertainment/", views.entertainment_events_view, name="entertainment_events_view"),
    path("exclusive/", views.exclusive_events_view, name="exclusive_events_view"),
    path("delete/<event_id>",views.delete_event_view, name="delete_event_view"),
    path("update/<event_id>/", views.update_event_view , name="update_event_view"),
    path("details/<event_id>", views.event_details_view , name="event_details_view"),
    path("search/", views.search_page_view, name="search_page_view"),
    path("ticket/", views.booking_page_view, name="booking_page_view"),

]
