from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from .models import Recipe, Review
from favorites.models import Favorite
from django.contrib.auth.models import User


# Create your views here.


def home_recipes_view(request: HttpRequest):
    
    if "sort" in request.GET and request.GET["sort"] == "oldest":
        recipes = Recipe.objects.all().order_by("published_at")[0:]
    else:
        recipes = Recipe.objects.all().order_by("-published_at")[0:]

    recipes_count = recipes.count()


    return render(request, "recipes/recipe_home.html", {"recipes" : recipes , "recipes_count" : recipes_count })



def add_recipe_view(request:HttpRequest):
      msg = None

      if request.method == "POST":

        try:
            new_recipe = Recipe(user=request.user, name=request.POST["name"], description=request.POST["description"], category=request.POST["category"] , preparing=request.POST["preparing"],ingredients=request.POST["ingredients"],picture = request.FILES["picture"] )
            new_recipe.save()
            return redirect("recipes:home_recipes_view")
        
        except Exception as e:
            msg = f"Please fill in all fields and try again. {e}"

      return render(request, "recipes/add_recipes.html", {"categories" : Recipe.categories,  "msg" : msg})



def recipe_detail_view(request:HttpRequest, recipe_id):
    try:
        recipe_detail = Recipe.objects.get(id=recipe_id)
        
        if request.method=="POST":
            review = Review(recipe=recipe_detail ,user=request.user ,review=request.POST["review"] , rating=request.POST["rating"])
            if 'image' in request.FILES: review.image = request.FILES["image"]
            review.save()
        # else:
        #     review=request.user.is_authenticated and Review.objects.filter(recipe=recipe_detail, user=request.user).exists()
        #     review.delete()
        

        reviews = Review.objects.filter(recipe=recipe_detail)


        reviews_count =reviews.count()

        is_favored = request.user.is_authenticated and Favorite.objects.filter(recipe=recipe_detail, user=request.user).exists()
    except Exception as e:
        return render(request, 'main/not_found.html')
    
    return render(request, "recipes/display_recipes.html", {"recipe" : recipe_detail , "reviews" : reviews , "reviews_count": reviews_count , "is_favored" : is_favored })



def update_recipe_view(request: HttpRequest, recipe_id):
    
    # if not request.user.is_authenticated:
    #     return render(request, 'main/not_authrized.html')

    recipe = Recipe.objects.get(id= recipe_id)

    if request.method == "POST":
         
        recipe.name = request.POST["name"]
        recipe.description = request.POST["description"]
        recipe.category = request.POST["category"]
        recipe.ingredients = request.POST["ingredients"]
        recipe.preparing = request.POST["preparing"]
        recipe.picture= request.FILES["picture"]
        recipe.save()

        return redirect('recipes:recipe_detail_view',  recipe_id=recipe.id)
    
    return render(request, "recipes/update_recipe.html", {"recipe" : recipe ,"categories"  : Recipe.categories})



def delete_recipe_view(request: HttpRequest, recipe_id):
    msg=None
    try:
       

        recipe = Recipe.objects.get(id=recipe_id)
        recipe.delete()
    except Exception as e:
        return render(request, 'main/not_found.html')
        
    return redirect("recipes:home_recipes_view")



def search_results_view(request: HttpRequest):
   
    if "search" in request.GET:
        keyword = request.GET["search"]
        recipes = Recipe.objects.filter(name__icontains=keyword )
        # recipes = Recipe.objects.filter(category__icontains=keyword )
        # recipes = User.objects.filter(username__icontains=keyword )
    else:
        recipes = Recipe.objects.all()
            
    recipe_count= recipes.count()
   
    return render(request, "recipes/search_recipe.html", {"recipes" : recipes , "recipe_count":recipe_count})
    


def recipe_category_view (request: HttpRequest):
    try:
        if "category" in request.GET and request.GET["category"] == "breakfast":
            recipe = Recipe.objects.filter(category__icontains="breakfast")

        elif "category" in request.GET and request.GET["category"] == "lunch":
            recipe = Recipe.objects.filter(category__icontains="lunch")

        elif "category" in request.GET and request.GET["category"] == "dinner":
            recipe = Recipe.objects.filter(category__icontains="dinner")

        elif "category" in request.GET and request.GET["category"] == "salad":
            recipe = Recipe.objects.filter(category__icontains="salad")

        elif "category" in request.GET and request.GET["category"] == "smoothie":
            recipe = Recipe.objects.filter(category__icontains="smoothie")

        elif "category" in request.GET and request.GET["category"] == "sweet":
            recipe = Recipe.objects.filter(category__icontains="sweet")
        else:
            recipe = Recipe.objects.all()

    except Exception as e:
        return render(request, 'main/not_found.html')
    
    recipe_count = recipe.count()
    return render(request, "recipes/recipe_home.html", {"recipes" : recipe , " recipe_count" :  recipe_count })


