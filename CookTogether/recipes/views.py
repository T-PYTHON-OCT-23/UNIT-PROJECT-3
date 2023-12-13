from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from recipes.models import Recipe,Comment
from ingredients.models import Ingredient
from favorites.models import Favorite

def add_recipe(request : HttpRequest):
    if not request.user.has_perm('recipes.add_recipe'):
        return render(request,'recipes/not_authorized.html')
    msg = None
    try:
        if request.method=='POST':
            recipe=Recipe(name=request.POST['name'],description=request.POST['description'],time=request.POST['time'],quantities_ingredients=request.POST['quantities_ingredients'],cal=request.POST['cal'],instructions=request.POST['instructions'],image=request.FILES['image'],category=request.POST['category'])
            recipe.save()
            return redirect('recipes:browse_recipes')
    except Exception as e:
        msg = f"Unfortunately, we encountered an issue. Please ensure all required fields are complete and try again. {e}"
    return render(request,'recipes/add_recipe.html',{'categories':Recipe.categories ,'msg':msg})

def browse_recipes(request : HttpRequest):
    msg = None
    try:
        recipes=Recipe.objects.all()
        recipes_with_favs = []
        for recipe in recipes:
            recipe.is_favored = request.user.is_authenticated and Favorite.objects.filter(recipe=recipe,user=request.user)
            recipes_with_favs.append(recipe)
    except Exception as e:
        msg = f"Unfortunately, we encountered an issue. Please try again later. {e}"
    return render(request,'recipes/browse_recipes.html',{'recipes':recipes_with_favs,'msg':msg})

def delete_recipe(request : HttpRequest,recipe_id):
    try:
        if not request.user.has_perm('recipes.delete_recipe'):
            return render(request,'recipes/not_authorized.html')
        recipe=Recipe.objects.get(id=recipe_id)
        recipe.delete()
        return redirect('recipes:browse_recipes')
    except Exception:
        return redirect('recipes:browse_recipes')

def detail_recipe(request : HttpRequest,recipe_id):
    try:
        recipe=Recipe.objects.get(id=recipe_id)
        ingredients=Ingredient.objects.exclude(recipe=recipe)
        is_favored=request.user.is_authenticated and Favorite.objects.filter(recipe=recipe,user=request.user)
        if request.method=='POST':
            new_comment=Comment(recipe=recipe,user=request.user,content=request.POST['content'],rating=request.POST['rating'])
            new_comment.save()
        comments=Comment.objects.filter(recipe=recipe)
    except Exception:
        return redirect('recipes:not_exist')
    return render(request,'recipes/detail_recipe.html',{'recipe':recipe,'ingredients':ingredients,'is_favored':is_favored,'comments':comments})

def update_recipe(request : HttpRequest,recipe_id):
    if not request.user.has_perm('recipes.change_recipe'):
        return render(request,'recipes/not_authorized.html')
    msg = None
    try:
        recipe=Recipe.objects.get(id=recipe_id)
        if request.method=='POST':
            recipe.name=request.POST['name']
            recipe.description=request.POST['description']
            recipe.cal=request.POST['cal']
            recipe.time=request.POST['time']
            recipe.instructions=request.POST['instructions']
            if 'image' in request.FILES:
                recipe.image=request.FILES['image']
            recipe.category=request.POST['category']
            recipe.quantities_ingredients=request.POST['quantities_ingredients']
            recipe.save()
            return redirect('recipes:detail_recipe',recipe_id=recipe.id)
    except Exception as e:
        msg = f"Unfortunately, we encountered an issue. Please ensure all required fields are complete and try again. {e}"
    return render(request,'recipes/update_recipes.html',{'recipe':recipe,'categories':Recipe.categories,'msg':msg})

def search_page(request : HttpRequest):
    msg = None
    try:
        if 'search' in request.GET:
            search_term=request.GET['search']
            recipe=Recipe.objects.filter(name__contains=search_term)
        else:
            recipe=Recipe.objects.all()
    except Exception as e:      
        msg = f"Unfortunately, we encountered an issue. Please try again later. {e}"
    return render(request,'recipes/search.html',{'recipes':recipe,'msg':msg})

def recipe_categories(request : HttpRequest,cat):
    msg = None
    try:
        recipe=Recipe.objects.filter(category=cat)
    except Exception as e:      
        msg = f"Unfortunately, we encountered an issue. Please try again later. {e}"
    return render(request,'recipes/search.html',{'recipes':recipe,'cat':cat,'msg':msg})

def not_exist(request : HttpRequest):
    return render(request,'recipes/not_exist.html')

def not_authorized(request : HttpRequest):
    return render(request,'recipes/not_authorized.html')

# Create your views here.
