from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from recipes.models import Recipe

# Create your views here.

def home_view (request :HttpRequest):
         return render(request, "main/home.html" )
