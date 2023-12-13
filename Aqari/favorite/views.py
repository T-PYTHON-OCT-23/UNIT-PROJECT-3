from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Favorite
from property.models import Property
# Create your views here.


def add_favorite_view(request:HttpRequest, property_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")

   
    try:

       
        property = Property.objects.get(id=property_id)

        
        user_favored = Favorite.objects.filter(user=request.user, property=property).first() #.first() bring the first Favorite object if exists else None
        
        if not user_favored:
           
            new_favorite = Favorite(user=request.user, property=property)
            new_favorite.save()
        else:
            
            user_favored.delete()

        return redirect("property:detail_property_view", property_id=property.id)
    except Exception as e:
        return redirect("main:home_view")
    


def my_favorites_view(request: HttpRequest):

    favorites = Favorite.objects.filter(user=request.user)

    return render(request, 'favorite/my_favorites.html', {"favorites" : favorites})
def my_favorites_view(request: HttpRequest):

    favorites = Favorite.objects.filter(user=request.user)

    return render(request, 'favorite/my_favorites.html', {"favorites" : favorites})




