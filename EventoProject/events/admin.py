from django.contrib import admin
from .models import Event, Ticket,Review


# Register your models here.


#to customize the display table in the admin panel (optional)
class Event_Info(admin.ModelAdmin):

    list_display = ('title', 'content', 'posting_date', 'category')



class ReviewModel(admin.ModelAdmin):
    list_display = ('user', 'event', 'rating', 'comment', 'created_at')
    list_filter = ('event',)

admin.site.register(Event, Event_Info)
admin.site.register(Review, ReviewModel)



