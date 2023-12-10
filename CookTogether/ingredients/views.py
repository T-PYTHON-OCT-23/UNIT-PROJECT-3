from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Ingredient
from recipes.models import Recipe


def add_ingredient(request : HttpRequest):
    if request.method=='POST':
        ingredient=Ingredient(name=request.POST['name'],description=request.POST['description'],image=request.FILES['image'])
        if 'brand' in request.POST:
            ingredient.brand=request.POST['brand']
        ingredient.save()
        return redirect('ingredients:browse_ingredients')
    return render(request,'ingredients/add_ingredient.html')

def browse_ingredients(request : HttpRequest):
    ingredients=Ingredient.objects.all()
    return render(request,'ingredients/browse_ingredients.html',{'ingredients':ingredients})

def delete_ingredient(request : HttpRequest,ingredient_id):
    ingredient=Ingredient.objects.get(id=ingredient_id)
    ingredient.delete()
    return redirect('ingredients:browse_ingredients')

def update_ingredient(request : HttpRequest,ingredient_id):
    ingredient=Ingredient.objects.get(id=ingredient_id)
    if request.method=='POST':
        ingredient.name=request.POST['name']
        ingredient.description=request.POST['description']
        if 'brand' in request.POST:
            ingredient.brand=request.POST['brand']
        if 'image' in request.FILES:
            ingredient.image=request.FILES['image']
        ingredient.save()
        return redirect('ingredients:browse_ingredients')
    return render(request,'ingredients/update_ingredient.html',{'ingredient':ingredient})

def add_ingredients_to_recipe(request:HttpRequest, recipe_id,ingredient_id):
    recipe=Recipe.objects.get(id=recipe_id)
    ingredient=Ingredient.objects.get(id=ingredient_id)
    recipe.ingredients.add(ingredient)
    return redirect('recipes:detail_recipe',recipe_id=recipe_id)

def delete_ingredients_from_recipe(request:HttpRequest, recipe_id,ingredient_id):
    recipe=Recipe.objects.get(id=recipe_id)
    ingredient=Ingredient.objects.get(id=ingredient_id)
    recipe.ingredients.remove(ingredient)
    return redirect('recipes:detail_recipe',recipe_id=recipe_id)

def detail_ingredient(request : HttpRequest,ingredient_id):
    ingredient=Ingredient.objects.get(id=ingredient_id)
    return render(request,'ingredients/detail_ingredient.html',{'ingredient':ingredient})

        


# Create your views here.
