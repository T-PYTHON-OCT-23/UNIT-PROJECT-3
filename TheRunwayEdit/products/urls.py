from django.urls import path
from . import views
app_name = "products"
urlpatterns = [
    path('add/product',views.add_product,name='add_product'),
    path('products/admin',views.admin_products,name='admin_products'),
    path('delete/product/<product_id>/',views.delete_product,name='delete_product')
]
