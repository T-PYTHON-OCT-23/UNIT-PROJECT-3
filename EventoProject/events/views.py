from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Event
# Create your views here.

def booking_page_view(request:HttpRequest):
    ticket = Event.objects.all()
    return render(request,"events/booking.html")


def add_event_view(request: HttpRequest):

    if request.method == "POST":
        event = Event(title=request.POST["title"],content=request.POST["content"], posting_date=request.POST["posting_date"],category=request.POST["category"],image=request.FILES["image"])
        event.save()

        return redirect("events:events_home_view")

    return render(request, "events/add_event.html", {"categories" : Event.categories})



def events_home_view(request: HttpRequest):
    events = Event.objects.all().order_by("posting_date")
    return render(request, "events/events_home.html", {"events" : events})


def art_events_view(request: HttpRequest):
    art_events = Event.objects.filter(category="Art")

    return render(request,"events/art_event.html",{"art_events": art_events} )



def tech_events_view(request: HttpRequest):
    tech_events = Event.objects.filter(category="Technology")

    return render(request,"events/tech_event.html",{"tech_events": tech_events} )


def entertainment_events_view(request:HttpRequest):
    enter_events = Event.objects.filter(category="Entertainment")

    return render(request,"events/entertainment_event.html",{"enter_events": enter_events} )


def exclusive_events_view(request:HttpRequest):
    exclusive_events = Event.objects.filter(category="Exclusive")

    return render(request,"events/exclusive_event.html",{"exclusive_events": exclusive_events})


    
def delete_event_view(request:HttpRequest,event_id):

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
   
    return render(request , "events/event_details.html", {"event_detail":event_detail})


def search_page_view(request:HttpRequest):

    if "search" in request.GET:
        keyword = request.GET["search"]
        events = Event.objects.filter(title__contains=keyword)
    else:
        events = Event.objects.all()

    return render(request,"events/search_page.html",{"events": events})