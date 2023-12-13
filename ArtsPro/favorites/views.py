


from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Favorite
from Art.models import Art



def add_favorite_view(request:HttpRequest, art_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    try:
        art = Art.objects.get(id=art_id)
        user_favored = Favorite.objects.filter(user=request.user, art=art).first() 
        

        if not user_favored:
           
            new_favorite = Favorite(user=request.user, art=art)
            new_favorite.save()
        else:
            user_favored.delete()
        return redirect("Art:art_detail_view", art_id=art.id)
    except Exception as e:
        return redirect("Art:art_home_view")


def my_favorites_view(request: HttpRequest):

    favorites = Favorite.objects.filter(user=request.user)

    return render(request, 'favorites/my_favorites.html', {"favorites" : favorites})
