from django.urls import path
from . import views

app_name = "expos"

urlpatterns = [ 
    path("add/news/", views.add_news_view, name="add_news_view"),
    path("", views.news_home_view, name="news_home_view"),
    path("event/", views.event_home_view, name="event_home_view"),
    path("detail/<news_id>/", views.news_detail_view, name="news_detail_view"),
    path("add/event/",views.add_event_view,name="add_event_view"),
    path("detail/<event_id>",views.event_detail_view,name="event_detail_view"),
    path("delete/<event_id>/", views.delete_event_view, name="delete_event_view"),
    path("update/<event_id>/", views.update_event_view, name="update_event_view"),
    path("reservation/<event_id>/",views.reservation_event_view, name="reservation_event_view")



]