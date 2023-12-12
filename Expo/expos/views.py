from django.shortcuts import render ,redirect
from django.http import HttpRequest , HttpResponse
from .models import *
from django.utils import timezone


# Create your views here.

def add_news_view(request: HttpRequest):
    if not request.user.is_staff:
        return render(request, 'main/not_auth.html', status=401)
    msg = None
    if request.method == "POST":
        try:
            new_news = News(title=request.POST["title"], content=request.POST["content"] ,  category=request.POST["category"])
            if 'poster' in request.FILES:
                new_news.poster = request.FILES["poster"]
            new_news.save()

            return redirect("expos:news_home_view")
        except Exception as e:
            msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, "expos/add_news.html" , {"categories" : News.categories , 'msg' :msg})


def news_home_view(request: HttpRequest):

    news = News.objects.all()
    if "search" in request.GET:
        keyword = request.GET["search"]
        news = News.objects.filter(title__icontains=keyword)
    else:
        news = News.objects.all()

    return render(request, "expos/news.html", {"news" :news })


def news_detail_view(request:HttpRequest, news_id):
    
        news = News.objects.get(id=news_id)
       

        return render(request, "expos/news_detail.html", {"news" : news })


def add_event_view(request: HttpRequest):
    if not request.user.is_staff:
        return render(request, 'main/not_auth.html', status=401)
    msg = None
    if request.method == "POST":
        try:
            new_event = Event(title=request.POST["title"], content=request.POST["content"], date=request.POST["date"],price=request.POST["price"])
            if 'poster' in request.FILES:
                new_event.poster = request.FILES["poster"]
            new_event.save()

            return redirect("expos:event_home_view")
        except Exception as e:
            msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, "expos/add_event.html" , {'msg' :msg})


def event_detail_view(request:HttpRequest,event_id):
    
        event = Event.objects.get(id=event_id)
        if request.method == "POST":
            nReview = Review(event=event, user=request.user, rating=request.POST["rating"], comment=request.POST["comment"])
            nReview.save()

        reviews = Review.objects.filter(event=event)
    
        return render(request, "expos/event_detail.html", {"event" : event ,"reviews":reviews })

def delete_event_view(request: HttpRequest, event_id):

    #check for delete permission on movie
    if not request.user.has_perm("expos.delete_event"):
        return render(request, "main/not_authorized.html", status=401)

    event = Event.objects.get(id=event_id)
    event.delete()

    return redirect("expos:event_home_view")

def delete_news_view(request: HttpRequest, news_id):

    #check for delete permission on movie
    if not request.user.has_perm("expos.delete_news"):
        return render(request, "main/not_authorized.html", status=401)

    news = Event.objects.get(id=news_id)
    news.delete()

    return redirect("expos:news_home_view")

def event_home_view(request: HttpRequest):

    event = Event.objects.all()

    if "search" in request.GET:
        keyword = request.GET["search"]
        event = Event.objects.filter(title__icontains=keyword)
    else:
        event = Event.objects.all()

    return render(request, "expos/event.html", {"event" :event })


def update_event_view(request: HttpRequest, event_id):


    if not request.user.is_staff:
        return render(request, "main/not_authorized.html", status=401)
    
    event = Event.objects.get(id=event_id)

    if request.method == "POST":
        event.title = request.POST["title"]
        event.content = request.POST["content"]
        event.date = request.POST["date"]
        if 'poster' in request.FILES:
            event.poster= request.FILES["poster"]
        event.price = request.POST["price"]
        event.save()

        return redirect('expos:event_detail_view', event_id=event.id)

    return render(request, "expos/update.html", {"event" : event })






