from django.contrib import admin
from .models import Event, Ticket


# Register your models here.


#to customize the display table in the admin panel (optional)
class Event_Info(admin.ModelAdmin):

    list_display = ('title', 'content', 'posting_date', 'category')

class Ticket_Info(admin.ModelAdmin):

    list_display = ('quantity','start_date')


admin.site.register(Event, Event_Info)
admin.site.register(Ticket, Ticket_Info)
