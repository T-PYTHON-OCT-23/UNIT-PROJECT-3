from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from recipes.models import Recipe
from .models import Favorite

def add_favorite_recipe(request:HttpRequest,recipe_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login_page')
    try:
        recipe=Recipe.objects.get(id=recipe_id)
        user_recipe=Favorite.objects.filter(user=request.user,recipe=recipe).first()
        if not user_recipe:
            new_recipe=Favorite(user=request.user,recipe=recipe)
            new_recipe.save()
        else:
            user_recipe.delete()

        if "next" in request.GET:
            return redirect('recipes:browse_recipes')
        else:
            return redirect('recipes:detail_recipe',recipe_id=recipe.id)
    except Exception:
        return redirect("recipes:browse_recipes")
    

def favorites_page(request:HttpRequest):
    msg = None
    try:
        favorites=Favorite.objects.filter(user=request.user)
    except Exception as e:
        msg = f"Unfortunately, we encountered an issue. Please try again later. {e}"
    return render(request,'favorites/favorites_page.html',{'favorites':favorites,'msg':msg})

def delete_favorite_recipe(request:HttpRequest,recipe_id):
    try:
        recipe=Recipe.objects.get(id=recipe_id)
        favorite=Favorite.objects.get(recipe=recipe,user=request.user)
        favorite.delete()
        return redirect('favorites:favorites_page')
    except Exception:
        return redirect('favorites:favorites_page')


# Create your views here.
