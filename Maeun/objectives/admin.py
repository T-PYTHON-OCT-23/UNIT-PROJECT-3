from django.contrib import admin
from .models import Objective , Order

# Register your models here.


#to customize the display table in the admin panel (optional)
class ObjectiveAdmin(admin.ModelAdmin):

    list_display = ('id','user','name', 'description', 'category', 'poster','reserved','created_at')
    list_filter = ('category', 'name','reserved')

class OrderAdmin(admin.ModelAdmin):

    list_display = ('objective','user', 'acceptance' ,'day', 'hour','created_at')
    list_filter = ('objective', 'user')



admin.site.register(Objective, ObjectiveAdmin)
admin.site.register(Order, OrderAdmin)

# Register your models here.
