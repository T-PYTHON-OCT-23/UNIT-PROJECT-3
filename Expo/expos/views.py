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
            new_news = News(title=request.POST["title"], content=request.POST["content"], publishd_at=timezone.now()  ,  category=request.POST["category"])
            if 'poster' in request.FILES:
                new_news.poster = request.FILES["poster"]
            new_news.save()

            return redirect("expos:expo_home_view")
        except Exception as e:
            msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, "expos/add_news.html" , {"categories" : News.categories , 'msg' :msg})


def expo_home_view(request: HttpRequest):

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