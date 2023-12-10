from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.


def my_orders_view(request: HttpRequest):

   # order = Favorite.objects.filter(user=request.user)

    return render(request, 'orders/my_orders.html')


def pay_view(request: HttpRequest):

   # order = Favorite.objects.filter(user=request.user)

    return render(request, 'orders/payment.html')