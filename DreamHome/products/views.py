from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Product

# Create your views here.

def add_products_view( request:HttpResponse):
   if request.method == "POST":
        new_products = Product(name=request.POST["name"], content=request.POST["content"],size=request.POST["size"],choose_co=request.POST["choose_co"],product=request.FILES["product"])
        new_products.save()
        
        return redirect("products:display_products_view")

   return render(request, "products/add_product.html" , {"choose_color" : Product.choose_color})


def display_products_view(request: HttpRequest):

     products = Product.objects.all()

     return render(request, "products/display.html", {"products": products})