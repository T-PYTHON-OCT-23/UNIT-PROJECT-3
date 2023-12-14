from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Product,Order,Repair

# Create your views here.

def repair_products_view(request:HttpRequest ):


    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    
    if request.method =="POST":
        new_repairs=Repair(full_name=request.POST["full_name"], number=request.POST["number"],city=request.POST["city"],address_details=request.POST["address_details"],total=request.POST["total"])
        new_repairs.save()

        return redirect("orders:repair_products_view")
    return render(request, "orders/repair.html", {"your_city" :Repair.your_city})



def add_order_view(request: HttpRequest, product_id):
 
   
   product = Product.objects.get(id=product_id)
   new_order =Order(product= product, user=request.user) 
   new_order.save()
      
   return redirect("orders:my_orders_view") 
    

    

def delete_order_view(request: HttpRequest, order_id):
    
    
   order = Order.objects.get(id=order_id)
   order.delete()

   return redirect("orders:my_orders_view")   



def my_orders_view(request: HttpRequest):
 try:
   orders = Order.objects.filter(user=request.user)

   total = 0

   for order in orders:
       total += float(order.product.product_price)

 except:
        return render(request, "accounts/login.html")   
 return render(request, 'orders/my_orders.html', {"orders" : orders, "total" : total})




def pay_view(request: HttpRequest):
    

   # order = Favorite.objects.filter(user=request.user)

    return render(request, 'orders/payment.html')


def shooping_backet_view(request: HttpRequest):

  

    return render(request, 'orders/shooping_backet.html')



def test_backet_view(request: HttpRequest):

  

    return render(request, 'orders/add_order.html')