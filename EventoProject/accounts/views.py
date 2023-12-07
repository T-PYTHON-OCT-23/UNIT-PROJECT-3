from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.


def register_user_view(request, HttpRequest):
    return render(request,"accounts/")
