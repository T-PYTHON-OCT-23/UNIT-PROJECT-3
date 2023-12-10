from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from recipes.models import Recipe,Comment
from ingredients.models import Ingredient
from favorites.models import Favorite


def add_recipe(request : HttpRequest):
    if request.method=='POST':
        recipe=Recipe(name=request.POST['name'],description=request.POST['description'],time=request.POST['time'],kall=request.POST['kall'],instructions=request.POST['instructions'],image=request.FILES['image'],category=request.POST['category'])
        recipe.save()
    return render(request,'recipes/add_recipe.html',{'categories':Recipe.categories})

def browse_recipes(request : HttpRequest):
    recipes=Recipe.objects.all()
    return render(request,'recipes/browse_recipes.html',{'recipes':recipes})

def delete_recipe(request : HttpRequest,recipe_id):
    recipe=Recipe.objects.get(id=recipe_id)
    recipe.delete()
    return redirect('recipes:browse_recipes')

def detail_recipe(request : HttpRequest,recipe_id):
    recipe=Recipe.objects.get(id=recipe_id)
    ingredients=Ingredient.objects.exclude(recipe=recipe)
    is_favored=request.user.is_authenticated and Favorite.objects.filter(recipe=recipe,user=request.user)
    if request.method=='POST':
        new_comment=Comment(recipe=recipe,user=request.user,content=request.POST['content'],rating=request.POST['rating'])
        new_comment.save()
    comments=Comment.objects.filter(recipe=recipe)
    return render(request,'recipes/detail_recipe.html',{'recipe':recipe,'ingredients':ingredients,'is_favored':is_favored,'comments':comments})

def update_recipe(request : HttpRequest,recipe_id):
    recipe=Recipe.objects.get(id=recipe_id)
    if request.method=='POST':
        recipe.name=request.POST['name']
        recipe.description=request.POST['description']
        recipe.kall=request.POST['kall']
        recipe.time=request.POST['time']
        recipe.instructions=request.POST['instructions']
        if 'image' in request.FILES:
            recipe.image=request.FILES['image']
        recipe.category=category=request.POST['category']
        recipe.save()
        return redirect('recipes:detail_recipe',recipe_id=recipe.id)
    return render(request,'recipes/update_recipes.html',{'recipe':recipe,'categories':Recipe.categories})

def search_page(request : HttpRequest):
    if 'search' in request.GET:
        search_term=request.GET['search']
        recipe=Recipe.objects.filter(name__contains=search_term)
    else:
       recipe=Recipe.objects.all()
    return render(request,'recipes/search.html',{'recipes':recipe})

def recipe_categories(request : HttpRequest,cat):
    recipe=Recipe.objects.filter(category=cat)
    return render(request,'recipes/search.html',{'recipes':recipe,'cat':cat})

def not_exist(request : HttpRequest):
    return render(request,'recipes/not_exist,html')
# Create your views here.
