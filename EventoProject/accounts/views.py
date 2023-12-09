from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def register_user_view(request, HttpRequest):

    if request.method == "POST":
        new_user = User.objects.create_new_user(first_name = request.POST["first_name"],last_name = request.POST["last_name"],username = request.POST["username"],email = request.POST["email"],password=request.POST["password"])
        new_user.save()

    return render(request,"accounts/register_page.html")
