from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Product,Review
from favorites.models import Favorite

# Create your views here.

def add_products_view(request:HttpRequest ):
    if request.method =="POST":
        new_products=Product(name=request.POST["name"], content=request.POST["content"],choose_product=request.POST["choose_product"],product_price=request.POST["product_price"],product=request.FILES["product"])
        new_products.save()

        return redirect("products:display_products_view")
    return render(request, "products/add_product.html" , {"choose_color" : Product.choose_color})

def display_products_view(request: HttpRequest):
    if "order" in request.GET and request.GET["order"] == "top":
        products = Product.objects.all().order_by("-product_price")[0:]
    else:
        products = Product.objects.all().order_by("product_price")[0:]
    
    return render(request, "products/display.html", {"products": products})


def product_detail_view(request:HttpRequest, product_id):
     
    if not request.user.is_authenticated:
         redirect("accounts:login_user_view")

    product_detail = Product.objects.get(id=product_id)
    try:

      if request.method == "POST":
         new_review = Review(product=product_detail, user=request.user, rating=request.POST["rating"], comment=request.POST["comment"])
         if 'image' in request.FILES: new_review .image=request.FILES["image"]
         new_review.save()
         return redirect("products:product_detail_view", product_detail.id)
    except Exception as e:
      return render(request, "products/not_exist.html")
    reviews = Review.objects.filter(product=product_detail.id)
    reviews_count= reviews.count()
    is_favored=request.user.is_authenticated and Favorite.objects.filter(product=product_detail, user=request.user).exists
    
   
    return render(request, "products/detail.html", {"product_detail" : product_detail , "reviews" : reviews , "reviews_count":reviews_count ,"is_favored":is_favored})

def not_exist_view(request:HttpRequest):

   return render(request, "products/not_exist.html")


def update_product_view(request: HttpRequest, product_id):
    if not request.user.is_staff:
        return render(request, "main/not_authorized.html", status=401)
    
    product = Product.objects.get(id=product_id)

    if request.method == "POST":
        product .name = request.POST["name"]
        product .content = request.POST["content"]
        product .choose_product = request.POST["choose_product"]
        product .product = request.POST["product"]
        product .save()

        return redirect('products:display_products_view', product=product.id)
    return render(request, "products/update.html", {"product" : product , "choose_color"  : Product.choose_color})

def delete_product_view(request: HttpRequest, product_id):
    
    
    if not request.user.is_staff:
        return render(request, "main/not_authorized.html", status=401)
    
    product = Product.objects.get(id=product_id)
    product.delete()

    return redirect("products:display_products_view")

def search_results_view(request: HttpRequest):

    if "search" in request.GET:
        keyword = request.GET["search"]
        products = Product.objects.filter(name__contains=keyword)
    else:
        products = Product.objects.all()

    return render(request, "products/searsh.html", {"products" : products})


def product_home_view_pro(request: HttpRequest,product ):

    if "order" in request.GET and request.GET["order"] == "top":
        products = Product.objects.all().order_by("-product_price")[0:]
    else:
        products = Product.objects.all().order_by("product_price")[0:]

    

    products_count = products.count()

    return render(request, "products/display.html", {"products" : products, "products_count" : products_count})

