from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Event, Ticket, Review
from favorites.models import Favorite
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage

#To add e new event 
def add_event_view(request: HttpRequest):

    if not request.user.is_staff:
        return render(request, "main/not_uth.html", status=401)

    if request.method == "POST":
        event = Event(title=request.POST["title"],content=request.POST["content"], posting_date=request.POST["posting_date"],category=request.POST["category"],image=request.FILES["image"],location=request.POST["location"])
        event.save()

        return redirect("events:events_home_view")

    return render(request, "events/add_event.html", {"categories" : Event.categories})


#To display the events in home page events
def events_home_view(request: HttpRequest):
    events = Event.objects.all().order_by("posting_date")
    return render(request, "events/events_home.html", {"events" : events})



#To delete the event only by the Admin 
def delete_event_view(request:HttpRequest,event_id):

    #check for delete permission on movie
    if not request.user.has_perm("events.delete_event"):
        return render(request, "main/not_uth.html", status=401)

    event= Event.objects.get(id=event_id)
    event.delete()

    return redirect("events:events_home_view")


#To update the event
def update_event_view(request: HttpRequest, event_id):

    if not request.user.has_perm('events.add_event'):
        return render(request, "main/not_uth.html", status=401)
    
    event = Event.objects.get(id=event_id)

    if request.method == "POST":
        event.title = request.POST["title"]
        event.content = request.POST["content"]
        event.posting_date = request.POST["posting_date"]
        event.category = request.POST["category"]
        event.image = request.FILES["image"]
        event.location = request.POST["location"]
        event.save()

        return redirect('events:event_details_view', event_id=event.id)

    return render(request,"events/update_event.html", {"event" : event, "categories": Event.categories})


#To display the content details of event
def event_details_view(request:HttpRequest, event_id):

    event_detail = Event.objects.get(id=event_id)
    reviews = Review.objects.filter(event=event_detail)
    tickets = Ticket.objects.filter(event=event_detail)


    is_favored = request.user.is_authenticated and Favorite.objects.filter(event=event_detail, user=request.user).exists()
   
    return render(request , "events/event_details.html", {"event_detail":event_detail, "is_favored": is_favored, "reviews":reviews})


#To search for events
def search_page_view(request:HttpRequest):

    if "search" in request.GET:
        keyword = request.GET["search"]
        events = Event.objects.filter(title__contains=keyword)
    else:
        events = Event.objects.all()

    return render(request,"events/search_page.html",{"events": events})




#To display the tickets page of the user
def my_tickets_view(request: HttpRequest):

    tickets = Ticket.objects.filter(user=request.user)

    return render(request, 'events/ticket_details.html', {"tickets" : tickets})


#To book a ticket by the user 
def add_ticket_view(request: HttpRequest, event_id):

    if request.method == "POST":

        if not request.user.is_authenticated:
            return render(request, "main/not_uth.html", status=401)

        event = Event.objects.get(id=event_id)
        new_ticket = Ticket(event=event, user=request.user, quantity=request.POST["quantity"])  
        new_ticket.save()

        tickets = Ticket.objects.filter(event=event)


        email_sent = False
        if request.method =='POST':
            name = request.user.username
            email = request.user.email
            quantity = request.POST['quantity']
            bill_content = f"Yay! {name} Thank you for your booking. ({quantity}) Tickets was booked successfully! Your ticket number is:(RX{new_ticket.id}) in {new_ticket.event.title} | Location :{new_ticket.event.location}. See you there!"
            send_mail(
                'The bill',#title
                bill_content, #message
                'settings.EMAIL_HOST_USER', #Sender if not avalaible considered 
                [email],#recive email
                fail_silently=False)
            email_sent = True

        return render(request, "events/the_bill.html",{"event_detail": event, "tickets":tickets})



#Events categories
def events_home_view_catego(request: HttpRequest, cat):

    if "order" in request.GET and request.GET["order"] == "top":
        events = Event.objects.filter(category=cat).order_by("-posting_date")
    else:
        events = Event.objects.filter(category=cat)

    events_count = events.count()

    return render(request, "events/events_home.html", {"events" : events, "events_count" : events_count})


def old_tickets_view(request: HttpRequest):

    tickets = Ticket.Event.objects.filter().order_by("posting_date")

    return render(request, "events/ticket_details.html", {"tickets":tickets})


#Filtering the events from the old events
def old_events_view(request: HttpRequest):

    events = Event.objects.filter().order_by("posting_date")

    return render(request, "events/events_home.html", {"events" : events})


#Filtering the events from the new events
def new_events_view(request: HttpRequest):

    events = Event.objects.filter().order_by("-posting_date")

    return render(request, "events/events_home.html", {"events" : events})




def add_review_view(request: HttpRequest, event_id):


    if request.method == "POST":

        if not request.user.is_authenticated:
            return render(request, "main/not_uth.html", status=401)

        event_id = Event.objects.get(id=event_id)
        new_review = Review(event=event_id, user=request.user, rating=request.POST["rating"], comment=request.POST["comment"])  
        new_review.save()
        return redirect("events:event_details_view", event_id=event_id.id)


def review_page_view(request:HttpRequest, event_id):

    event_detail = Event.objects.get(id=event_id)
    reviews = Review.objects.filter(event=event_detail)
    return render(request,"events/review_page.html",{"event_detail":event_detail,"reviews":reviews})