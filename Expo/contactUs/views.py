from django.shortcuts import render, redirect
from django.http import HttpRequest , HttpResponse

from .models import Contact

# Create your views here.

def contact_view(request:HttpRequest):
    if request.method == 'POST':
        new_message = Contact(name=request.POST['name'],email=request.POST['email'],subject = request.POST['subject'],message = request.POST['message'],status='Unread')
        new_message.save()
        return redirect('contactUs:thank_you_view')
    return render(request, 'contactUs/contact.html')

def thank_you_view(request:HttpRequest):
    
    return render(request, 'contactUs/thank_you.html')

