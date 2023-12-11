from django.urls import path
from . import views
app_name = "events"


urlpatterns = [

    path("", views.events_home_view, name="events_home_view"),
    path("add/", views.add_event_view, name="add_event_view"),
    path("delete/<event_id>",views.delete_event_view, name="delete_event_view"),
    path("update/<event_id>/", views.update_event_view , name="update_event_view"),
    path("details/<event_id>", views.event_details_view , name="event_details_view"),
    path("search/", views.search_page_view, name="search_page_view"),
    path("bill/<event_id>/", views.the_bill_view, name="the_bill_view"),
    path("ticket/<event_id>/", views.add_ticket_view , name="add_ticket_view"),
    path("category/<cat>/", views.events_home_view_catego, name="events_home_view_catego")

]
