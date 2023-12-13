from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Ingredient
from recipes.models import Recipe


def add_ingredient(request : HttpRequest):
    if not request.user.is_superuser:
        return render(request,'recipes/not_authorized.html')
    msg = None
    try:
        if request.method=='POST':
            ingredient=Ingredient(name=request.POST['name'],description=request.POST['description'],image=request.FILES['image'])
            if 'brand' in request.POST:
                ingredient.brand=request.POST['brand']
            ingredient.save()
            return redirect('ingredients:browse_ingredients')
    except Exception as e:
        msg = f"Unfortunately, we encountered an issue. Please ensure all required fields are complete and try again. {e}"
    return render(request,'ingredients/add_ingredient.html',{'msg':msg})

def browse_ingredients(request : HttpRequest):
    if not request.user.is_superuser:
        return render(request,'recipes/not_authorized.html')    
    msg = None
    try:
        ingredients=Ingredient.objects.all()
    except Exception as e:
        msg = f"We're experiencing technical difficulties right now. Please try again later. {e}"
    return render(request,'ingredients/browse_ingredients.html',{'ingredients':ingredients,'msg':msg})
    

def delete_ingredient(request : HttpRequest,ingredient_id):
    if not request.user.is_superuser:
        return render(request,'recipes/not_authorized.html')
    ingredient=Ingredient.objects.get(id=ingredient_id)
    ingredient.delete()
    return redirect('ingredients:browse_ingredients')

def update_ingredient(request : HttpRequest,ingredient_id):
    if not request.user.is_superuser:
        return render(request,'recipes/not_authorized.html')
    msg = None
    try:
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
    except Exception as e:
        msg = f"We're experiencing technical difficulties right now. Please try again later. {e}"
    return render(request,'ingredients/update_ingredient.html',{'ingredient':ingredient,'msg':msg})

def add_ingredients_to_recipe(request:HttpRequest, recipe_id,ingredient_id):
    if not request.user.is_superuser:
        return render(request,'recipes/not_authorized.html')
    recipe=Recipe.objects.get(id=recipe_id)
    ingredient=Ingredient.objects.get(id=ingredient_id)
    recipe.ingredients.add(ingredient)
    return redirect('recipes:detail_recipe',recipe_id=recipe_id)

def delete_ingredients_from_recipe(request:HttpRequest, recipe_id,ingredient_id):
    if not request.user.is_superuser:
        return render(request,'recipes/not_authorized.html')
    recipe=Recipe.objects.get(id=recipe_id)
    ingredient=Ingredient.objects.get(id=ingredient_id)
    recipe.ingredients.remove(ingredient)
    return redirect('recipes:detail_recipe',recipe_id=recipe_id)

def detail_ingredient(request : HttpRequest,ingredient_id):
    if not request.user.is_superuser:
        return render(request,'recipes/not_authorized.html')
    try:
        ingredient=Ingredient.objects.get(id=ingredient_id)
    except Exception:
        return redirect('recipes:not_exist')
    return render(request,'ingredients/detail_ingredient.html',{'ingredient':ingredient})

        


# Create your views here.
