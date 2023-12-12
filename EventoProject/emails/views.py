from django.shortcuts import render ,redirect
from django.http import HttpResponse ,HttpRequest
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from events.models import Event ,Ticket

# Create your views here.


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




