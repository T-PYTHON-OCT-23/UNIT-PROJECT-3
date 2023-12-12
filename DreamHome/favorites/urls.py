from django.urls import path
from . import views

app_name = "favorites"

urlpatterns = [
    path('<product_id>/add/', views.add_favorite_view, name="add_favorite_view"),
    path('', views.my_favorites_view, name="my_favorites_view")
   
]
