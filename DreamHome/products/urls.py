from django.urls import path
from . import views

app_name = "products"

urlpatterns = [ 
    path("", views.display_products_view, name="display_products_view"),
    path("add/", views.add_products_view, name="add_products_view"),
]