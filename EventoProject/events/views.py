from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Event, Ticket
from favorites.models import Favorite

def add_event_view(request: HttpRequest):

    if request.method == "POST":
        event = Event(title=request.POST["title"],content=request.POST["content"], posting_date=request.POST["posting_date"],category=request.POST["category"],image=request.FILES["image"])
        event.save()

        return redirect("events:events_home_view")

    return render(request, "events/add_event.html", {"categories" : Event.categories})



def events_home_view(request: HttpRequest):
    events = Event.objects.all().order_by("posting_date")
    return render(request, "events/events_home.html", {"events" : events})



    
def delete_event_view(request:HttpRequest,event_id):

    #check for delete permission on movie
    if not request.user.has_perm("events.delete_event"):
        return render(request, "main/not_uth.html", status=401)

    event= Event.objects.get(id=event_id)
    event.delete()

    return redirect("events:events_home_view")


def update_event_view(request: HttpRequest, event_id):

    event = Event.objects.get(id=event_id)
    if request.method == "POST":
        event.title = request.POST["title"]
        event.content = request.POST["content"]
        event.posting_date = request.POST["posting_date"]
        event.category = request.POST["category"]
        event.image = request.FILES["image"]
        event.save()

        return redirect('events:event_details_view', event_id=event.id)

    return render(request,"events/update_event.html", {"event" : event, "categories": Event.categories})


def event_details_view(request:HttpRequest, event_id):

    event_detail = Event.objects.get(id=event_id)

    is_favored = request.user.is_authenticated and Favorite.objects.filter(event=event_detail, user=request.user).exists()
   
    return render(request , "events/event_details.html", {"event_detail":event_detail, "is_favored": is_favored})


def search_page_view(request:HttpRequest):

    if "search" in request.GET:
        keyword = request.GET["search"]
        events = Event.objects.filter(title__contains=keyword)
    else:
        events = Event.objects.all()

    return render(request,"events/search_page.html",{"events": events})

def booking_page_view(request:HttpRequest):
    return render(request,"events/booking.html")

def the_bill_view(request:HttpRequest, event_id):
        
    event_detail = Event.objects.get(id=event_id)
    tickets = Ticket.objects.filter(event=event_detail)
    all_tickets = Ticket.objects.all()

    return render(request,"events/the_bill.html",{"event_detail":event_detail, "tickets":tickets, "all_tickets":all_tickets})


def add_ticket_view(request: HttpRequest, event_id):

    if request.method == "POST":

        if not request.user.is_authenticated:
            return render(request, "main/not_uth.html", status=401)

        event_id = Event.objects.get(id=event_id)
        new_ticket = Ticket(event=event_id, user=request.user, quantity=request.POST["quantity"])  
        new_ticket.save()
        return redirect("events:the_bill_view", event_id=event_id.id )


def events_home_view_catego(request: HttpRequest, cat):

    if "order" in request.GET and request.GET["order"] == "top":
        events = Event.objects.filter(category=cat).order_by("-posting_date")[0:10]
    else:
        events = Event.objects.filter(category=cat).order_by("-posting_date")[0:10]

    events_count = events.count()

    return render(request, "events/events_home.html", {"events" : events, "events_count" : events_count})




def old_events_view(request: HttpRequest):

    events = Event.objects.filter().order_by("posting_date")

    return render(request, "events/events_home.html", {"events" : events})



def new_events_view(request: HttpRequest):

    events = Event.objects.filter().order_by("-posting_date")

    return render(request, "events/events_home.html", {"events" : events})




