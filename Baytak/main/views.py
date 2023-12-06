from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse


def homePage(request : HttpRequest):

    return render(request ,"main/homePage.html")

