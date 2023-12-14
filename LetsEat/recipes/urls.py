from django.urls import path 
from . import views


app_name = "recipes"

urlpatterns = [
    path("" , views.home_recipes_view , name="home_recipes_view"),
    path("add/" , views.add_recipe_view , name="add_recipe_view"),
    path("detail/<recipe_id>/" , views.recipe_detail_view , name="recipe_detail_view"),
    path("update/<recipe_id>/" , views.update_recipe_view , name="update_recipe_view"),
    path("delete/<recipe_id>/" , views.delete_recipe_view , name="delete_recipe_view"),
    path("search/", views.search_results_view, name="search_results_view"),
    path("category/", views.recipe_category_view, name="recipe_category_view"),


   
]
