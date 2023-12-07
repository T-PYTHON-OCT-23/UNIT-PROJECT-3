from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Event


# Create your views here.

def add_event_view(request: HttpRequest):
    #Creating a new entry into the database for an event
    if request.method == "POST":
        new_event = Event(title=request.POST["title"], description=request.POST["description"],release_date=request.POST["release_date"], category=request.POST["category"])
        new_event.save()
        return redirect("events:event_home_view")
    return render(request, "events/add_event.html", {"categories" : Event.categories})



def event_home_view(request: HttpRequest):
    events = Event.objects.all()
    events_count = events.count()
    return render(request, "events/events_home.html", {"events" : events , "events_count":events_count})

def event_detail_view(request:HttpRequest, event_id):

    event = Event.objects.get(id=event_id)

    return render(request, "events/events_details.html", {"event" : event})



def delete_event_view(request: HttpRequest, event_id):

    event = Event.objects.get(id=event_id)
    event.delete()

    return redirect("events:event_home_view")
