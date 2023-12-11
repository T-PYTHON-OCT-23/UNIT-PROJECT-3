from django.contrib import admin
from .models import StableHorses ,ServicesStable
# Register your models here.

class StableHorsesModel(admin.ModelAdmin):
    list_display = ('name', 'description','city' ,'rating')
    list_filter = ('rating','city')

class ServicesStableModel(admin.ModelAdmin):
    list_display = ('stbleHorse','name_Servic', 'duration_service','price')
    list_filter = ('price','duration_service')

admin.site.register(StableHorses, StableHorsesModel)

admin.site.register(ServicesStable, ServicesStableModel)

