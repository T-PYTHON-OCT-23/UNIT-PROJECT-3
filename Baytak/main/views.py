from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse


def homePage(request : HttpRequest):

    return render(request ,"main/homePage.html")

def contact(request : HttpRequest):

    return render(request ,"main/contact.html")

def about(request : HttpRequest):

    return render(request ,"main/about.html")

