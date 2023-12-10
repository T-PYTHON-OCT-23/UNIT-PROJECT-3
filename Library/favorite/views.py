from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Favorite
from books.models import Book



def add_favorite(request:HttpRequest, book_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user")

    try:
        book = Book.objects.get(id=book_id)
        user_favored = Favorite.objects.filter(user=request.user, book=book).first() 
        
        if not user_favored:
            new_favorite = Favorite(user=request.user, book=book)
            new_favorite.save()
        else:

            user_favored.delete()

        return redirect("books:book_detail_view", book_id=book.id)
    except Exception as e:
         return redirect("main:home")
    



def fav(request: HttpRequest):

    favorites = Favorite.objects.filter(user=request.user)

    return render(request, 'favorite/fav.html', {"favorites" : favorites})

# Create your views here.
