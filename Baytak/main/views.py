from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact



def homePage(request : HttpRequest):

    return render(request ,"main/homePage.html")

def contact(request : HttpRequest):
    if request.method == "POST":
        
        newBlog = Contact(comment = request.POST["comment"] , requestType = request.POST["requestType"], evaluation = request.POST["evaluation"] )
        newBlog.save()
        return redirect("main:displayContact")

    return render(request, "main/contact.html" )
    
def about(request : HttpRequest):

    return render(request ,"main/about.html")

def thank(request : HttpRequest):

    return render(request ,"main/thankPage.html")

def displayContact(request : HttpRequest):
     contact = Contact.objects.all()

     return render(request ,"main/displayContact.html", {"contact" : contact})


