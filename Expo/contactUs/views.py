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

def message_view(request:HttpRequest,):
    message = Contact.objects.all()

    return render(request, "contactUs/messages.html", {"message" :message})

def status_view(request:HttpRequest,message_id):

    if not request.user.is_staff:
        return render(request, "main/not_authorized.html", status=401)
    
    message = Contact.objects.get(id=message_id)

    if request.method == "POST":

        message.status = request.POST["status"]
        message.save()
    
        return redirect('contactUs:display_message_view' ,message_id)
    
    return render(request, 'contactUs/update_status.html',{"message": message ,"status_choices":Contact.status_choices})

def display_message_view(request:HttpRequest ,message_id):
    message = Contact.objects.get(id=message_id)
    
    return render(request, "contactUs/display_message.html", {"message" : message })




