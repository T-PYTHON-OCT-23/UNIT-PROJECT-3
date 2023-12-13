from django.urls import path
from . import views
app_name = "recipes"
urlpatterns = [
    path('add/recipe',views.add_recipe,name='add_recipe'),
    path('recipes',views.browse_recipes,name='browse_recipes'),
    path('delete/recipe/<recipe_id>/',views.delete_recipe,name='delete_recipe'),
    path('detail/recipe/<recipe_id>/',views.detail_recipe,name='detail_recipe'),
    path('update/recipe/<recipe_id>/',views.update_recipe,name='update_recipe'),
    path('search/page',views.search_page,name='search_page'),
    path('recipe/categories/<cat>/',views.recipe_categories,name='recipe_categories'),
    path('not/exist',views.not_exist,name='not_exist'),
    path('not/authorized',views.not_authorized,name='not_authorized')
]