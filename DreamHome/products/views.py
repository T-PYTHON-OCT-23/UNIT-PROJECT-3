from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Product,Review

# Create your views here.

def add_products_view(request:HttpRequest):
    if request.method =="POST":
        new_products=Product(name=request.POST["name"], content=request.POST["content"],size=request.POST["size"],choose_product=request.POST["choose_product"],product=request.FILES["product"])
        new_products.save()

        return redirect("products:display_products_view")
    return render(request, "products/add_product.html" , {"choose_color" : Product.choose_color})

def display_products_view(request: HttpRequest):

     products = Product.objects.all()
    
     return render(request, "products/display.html", {"products": products})


def product_detail_view(request:HttpRequest, product_id):

    product_detail = Product.objects.get(id=product_id)
    

    return render(request, "products/detail.html", {"product_detail" : product_detail})


def delete_product_view(request: HttpRequest, product_id):
    
    product = Product.objects.get(id=product_id)
    product.delete()

    return redirect("products:display_products_view")