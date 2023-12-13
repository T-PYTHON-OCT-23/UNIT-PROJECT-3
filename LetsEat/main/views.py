from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from recipes.models import Recipe , Review
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test





# Create your views here.

def home_view (request :HttpRequest):
      
    latest_review = Review.objects.all().order_by("-date")[0:5]

    return render(request, "main/home.html" , {"latest_review": latest_review})


def about_view (request :HttpRequest):
         return render(request, "main/about.html" )


