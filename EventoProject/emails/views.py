from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from events.models import Event
# Create your views here.

def contact_us_view(request):
    email_sent = False
    if request.method =='POST':
        message = request.POST["message"]
        email = request.POST["email"]
        name = request.POST['name']
        message_content = f"{email} sent you a message : \n {message}"
        send_mail(
            'Contact Form',#title
            message_content, #message
            'settings.EMAIL_HOST_USER', #Sender if not avalaible considered 
            ["sufanamarouf1@gmail.com"],#recive email
            fail_silently=False)
        
        email_sent = True
    return render(request,"emails/contact_us.html", {"email_sent" : email_sent})


def the_bill_view(request):

    
    email_sent = False
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST["email"]
        quantity = request.POST['quantity']
        bill_content = f"Yay! {name} Thank you for your purchase. Please find the bill attached.{quantity} Tickets was booked successfully!"
        send_mail(
            'The bill',#title
            bill_content, #message
            'settings.EMAIL_HOST_USER', #Sender if not avalaible considered 
            [email],#recive email
            fail_silently=False)
        
        email_sent = True
    return render(request,"emails/book.html", {"email_sent" : email_sent})

