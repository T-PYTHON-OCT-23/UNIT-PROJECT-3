from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from .models import Favorite
from recipes.models import Recipe
# Create your views here.


def add_favorite_view(request:HttpRequest, recipe_id):

    if not request.user.is_authenticated:
        return redirect("accounts:sign_in_view")
    try:
        recipe = Recipe.objects.get(id=recipe_id)

        is_favored = Favorite.objects.filter(user=request.user, recipe=recipe).first() 
        
        if not is_favored:
            new_favorite = Favorite(user=request.user, recipe=recipe)
            new_favorite.save()
        else:
            is_favored.delete()

        return redirect("recipes:recipe_detail_view", recipe_id=recipe.id)
    except Exception as e:
        return redirect("main:home_view")
    


def my_favorites_view(request: HttpRequest):

    favorites = Favorite.objects.filter(user=request.user)

    return render(request, 'favorites/display_fav.html', {"favorites" : favorites})




