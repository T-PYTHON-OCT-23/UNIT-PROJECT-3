from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
   path('', views.my_orders_view, name="my_orders_view"),
    path("pay/", views.pay_view, name="pay_view")
]  