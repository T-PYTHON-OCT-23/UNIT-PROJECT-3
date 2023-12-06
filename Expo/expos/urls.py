from django.urls import path
from . import views

app_name = "expos"

urlpatterns = [ 
    path("add/", views.add_news_view, name="add_news_view"),
    path("", views.expo_home_view, name="expo_home_view"),
    path("detail/<news_id>/", views.news_detail_view, name="news_detail_view"),
]