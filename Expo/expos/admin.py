from django.contrib import admin
from .models import *



class ReviewModel(admin.ModelAdmin):
    list_display = ('user', 'event', 'created_at')
    list_filter = ('event',)

admin.site.register(Review, ReviewModel)
admin.site.register(News)
admin.site.register(Reservation)

# Register your models here.
