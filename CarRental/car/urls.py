from django.urls import path
from . import views

app_name = "car"

urlpatterns = [
    path("add/",views.add_car_view,name="add_car_view"),
    path("",views.cars_view,name="cars_view"),
    path("details/<str:pk>",views.cars_details_view,name="cars_details_view"),
    path("update/<str:pk>",views.cars_update_view,name="cars_update_view"),
    path("delet/<str:pk>",views.cars_delete_view,name="cars_delete_view"),
    path("search/",views.car_search_view,name="car_search_view"),
    path("booking/search/",views.booking_search_view,name="booking_search_view"),
    path("booking/search/<str:pk>",views.add_review_view,name="add_review_view")
]