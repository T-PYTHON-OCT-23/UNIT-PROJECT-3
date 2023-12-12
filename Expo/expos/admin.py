from django.contrib import admin
from .models import *



class ReviewModel(admin.ModelAdmin):
    list_display = ('user', 'event', 'created_at')
    list_filter = ('event',)

admin.site.register(Review, ReviewModel)
admin.site.register(News)

# Register your models here.
