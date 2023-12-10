from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from recipes.models import Recipe
from .models import Favorite

def add_favorite_recipe(request:HttpRequest,recipe_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login_page')
    recipe=Recipe.objects.get(id=recipe_id)
    user_recipe=Favorite.objects.filter(user=request.user,recipe=recipe).first()
    if not user_recipe:
        new_recipe=Favorite(user=request.user,recipe=recipe)
        new_recipe.save()
    else:
        user_recipe.delete()
    return redirect('recipes:detail_recipe',recipe_id=recipe.id)

def favorites_page(request:HttpRequest):
    favorites=Favorite.objects.filter(user=request.user)
    return render(request,'favorites/favorites_page.html',{'favorites':favorites})

# Create your views here.
