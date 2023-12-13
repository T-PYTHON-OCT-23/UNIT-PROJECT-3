from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from recipes.models import Recipe


def home_page(request : HttpRequest):
    msg=None
    try:
        recipes=Recipe.objects.all()[0:6]
    except Exception as e:
        msg = f"Unfortunately, we encountered an issue. Please try again later. {e}"
    return render(request,'main/home_page.html',{'recipes':recipes,'msg':msg})
