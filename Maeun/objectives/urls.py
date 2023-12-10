from django.urls import path
from . import views

app_name = "objectives"

urlpatterns = [
    path("add/",views.add_view, name="add_view"),
    path("",views.show_objectives,name="show_objectives"),
    path("my/",views.my_objectives_view,name="my_objectives_view"),
    path("delete/<obj_id>/", views.delete_objective_view,name="delete_objective_view"),
    path("update/<obj_id>/",views.update_objective_view,name="update_objective_view")
    
]