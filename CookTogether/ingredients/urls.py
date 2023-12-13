from django.urls import path
from . import views
app_name = "ingredients"
urlpatterns = [
    path('add/ingredient',views.add_ingredient,name='add_ingredient'),
    path('browse/ingredients',views.browse_ingredients,name='browse_ingredients'),
    path('delete/ingredient/<ingredient_id>/',views.delete_ingredient,name='delete_ingredient'),
    path('update/ingredient/<ingredient_id>/',views.update_ingredient,name='update_ingredient'),
    path('add/ingredients/to/recipe/<recipe_id>/<ingredient_id>/',views.add_ingredients_to_recipe,name='add_ingredients_to_recipe'),
    path('delete/ingredients/from/recipe/<recipe_id>/<ingredient_id>/',views.delete_ingredients_from_recipe,name='delete_ingredients_from_recipe'),
    path('detail/ingredient/<ingredient_id>/',views.detail_ingredient,name='detail_ingredient'),
    path('not/exist/ingredient',views.not_exist_ingredient,name='not_exist_ingredient')
]