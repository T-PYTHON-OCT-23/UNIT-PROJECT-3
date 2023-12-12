from django.contrib import admin
from .models import Objective

# Register your models here.


#to customize the display table in the admin panel (optional)
class ObjectiveAdmin(admin.ModelAdmin):

    list_display = ('id','name', 'description', 'category', 'poster','reserved','created_at')
    list_filter = ('category', 'name','reserved')





admin.site.register(Objective, ObjectiveAdmin)
# Register your models here.
