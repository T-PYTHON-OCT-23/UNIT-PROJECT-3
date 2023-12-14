from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
   path('', views.my_orders_view, name="my_orders_view"),
   path("pay/", views.pay_view, name="pay_view"),
   path('add/<product_id>/',views.add_order_view, name="add_order_view"),
   path('delete/<order_id>/', views.delete_order_view, name="delete_order_view"),
   path('repair/', views.repair_products_view, name="repair_products_view"),
   path('order/', views.shooping_backet_view, name="shooping_backet_view"),
 
]  