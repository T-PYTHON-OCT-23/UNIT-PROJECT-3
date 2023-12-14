from django.urls import path
from . import views

app_name = "objectives"

urlpatterns = [
    path("add/",views.add_view, name="add_view"),
    path("",views.show_objectives,name="show_objectives"),
    path("my/",views.my_objectives_view,name="my_objectives_view"),
    path("delete/<obj_id>/", views.delete_objective_view,name="delete_objective_view"),
    path("update/<obj_id>/",views.update_objective_view,name="update_objective_view"),
    path("borrowed/",views.my_objectives_borrowed_view,name="my_objectives_borrowed_view"),
    path("retrieved/<obj_id>/",views.objective_retrieved_view,name="objective_retrieved_view"),
    path("order/<obj_id>/",views.objective_order_view,name="objective_order_view"),
    path("loan/requests/",views.loan_requests_view,name="loan_requests_view"),
    path("order/rejection/<order_id>/",views.order_rejection_view,name="order_rejection_view"),
    path("order/acceptance/<order_id>/",views.order_acceptance_view,name="order_acceptance_view"),
    path("my/order/",views.my_order_view,name="my_order_view"),
    path("borrowed/objectives",views.borrowed_objectives_view,name="borrowed_objectives_view")

 
]