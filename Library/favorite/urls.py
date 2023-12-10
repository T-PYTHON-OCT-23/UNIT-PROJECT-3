from django.urls import path 
from . import views 


app_name  = "favorite"

urlpatterns = [
    path('<book_id>/add/', views.add_favorite, name="add_favorite"),
    path('', views.fav, name="fav")
]
