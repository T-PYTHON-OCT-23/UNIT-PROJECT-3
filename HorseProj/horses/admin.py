from django.contrib import admin
from .models import StableHorses
# Register your models here.

class StableHorsesModel(admin.ModelAdmin):
    list_display = ('name', 'description','city' ,'rating')
    list_filter = ('rating','city')


admin.site.register(StableHorses, StableHorsesModel)

