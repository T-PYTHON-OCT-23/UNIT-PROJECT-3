from django.urls import path
from . import views

app_name = "products"

urlpatterns = [ 
    path("", views.display_products_view, name="display_products_view"),
    path("add/", views.add_products_view, name="add_products_view"),
    path("detail/<product_id>/", views.product_detail_view , name="product_detail_view"),
    path("delete/<product_id>/", views.delete_product_view, name="delete_product_view"),
]