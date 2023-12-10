from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Favorite
from events.models import Event, Ticket
# Create your views here.


def add_favorite_view(request:HttpRequest, event_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")

    try:
        event = Event.objects.get(id=event_id)

        user_favored = Favorite.objects.filter(user=request.user, event=event).first() 
        
        if not user_favored:
            new_favorite = Favorite(user=request.user, event=event)
            new_favorite.save()
        else:
            user_favored.delete()

        return redirect("events:event_details_view", event_id=event.id)
    except Exception as e:
        return redirect("main:home_page_view")
    


def my_favorites_view(request: HttpRequest):

    favorites = Favorite.objects.filter(user=request.user)

    return render(request, 'favorites/my_favorites.html', {"favorites" : favorites})




