from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from books.models import Book, Review

# Create your views here.


def home_view(request: HttpRequest):

    books = Book.objects.all().order_by("-release_date")[0:8]
    reviews = Review.objects.all().order_by("-created_at")[0:8]
    
    if request.user.is_authenticated:
        print(request.user.first_name)

       

    return render(request, "main/home.html", {"books" : books, "reviews" : reviews})



def error(request : HttpRequest):
    return render(request,'main/not_authorized.html')