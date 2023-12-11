from django.urls import path
from . import views
app_name = "favorites"
urlpatterns = [
    path('add/favorite/recipe/<recipe_id>/',views.add_favorite_recipe,name='add_favorite_recipe'),
    path('favorites/page',views.favorites_page,name='favorites_page'),
    path('delete/favorite/recipe/<recipe_id>/',views.delete_favorite_recipe,name='delete_favorite_recipe')
]
