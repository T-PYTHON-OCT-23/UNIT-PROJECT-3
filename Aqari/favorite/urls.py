from django.urls import path
from . import views

app_name = "favorite"

urlpatterns = [path('<property_id>/add/', views.add_favorite_view, name="add_favorite_view"),
    path('', views.my_favorites_view, name="my_favorites_view")
]