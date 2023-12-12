from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.

def home_page_view(request: HttpRequest):
    return render(request,"main/index.html")



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
    return render(request,"main/contact_us.html", {"email_sent" : email_sent})
