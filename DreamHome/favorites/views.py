from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Favorite
from products.models import Product
# Create your views here.


def add_favorite_view(request:HttpRequest, product_id):

    product = Product.objects.get(id=product_id)
    user_favored = Favorite.objects.filter(user=request.user, product=product).first() 
    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
       
    try:
            
        if not user_favored:
            
            new_favorite = Favorite(user=request.user, product=product)
            new_favorite.save()
            return redirect("products:product_detail_view", product_id=product.id)
        else:
            user_favored.delete()
            return redirect("products:product_detail_view", product_id=product.id)
    except Exception as e:
        return redirect("main:home_view")
    
    


def my_favorites_view(request: HttpRequest):

    favorites = Favorite.objects.filter(user=request.user)

    return render(request, 'favorites/favorites.html', {"favorites" : favorites})





