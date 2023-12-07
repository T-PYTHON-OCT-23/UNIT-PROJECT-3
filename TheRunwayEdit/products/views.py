from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Product

def add_product(request:HttpRequest):
    if request.method=='POST':
        product=Product(name=request.POST['name'],description=request.POST['description'],price=request.POST['price'],brand=request.POST['brand'],image=request.FILES['image'],category=request.POST['category'])
        product.save()
    return render(request,'products/add_product.html',{'categories':Product.categories})

def admin_products(request : HttpRequest):
    product=Product.objects.all()
    return render(request, "products/admin_products.html", {"products" : product})

def delete_product(request : HttpRequest,product_id):
    product=Product.objects.get(id=product_id)
    product.delete()
    return redirect('products:admin_products')
# Create your views here.
