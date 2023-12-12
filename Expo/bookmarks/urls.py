from django.urls import path
from . import views

app_name = "bookmarks"

urlpatterns = [
    path('<news_id>/add/', views.add_bookmark_view, name="add_bookmark_view"),
    path('', views.my_bookmark_view, name="my_bookmark_view")
]