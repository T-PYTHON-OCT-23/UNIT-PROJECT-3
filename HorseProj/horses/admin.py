from django.contrib import admin
from .models import StableHorses ,ServicesStable,Reviews
# Register your models here.

class StableHorsesModel(admin.ModelAdmin):
    list_display = ('name', 'description','city' ,'rating')
    list_filter = ('rating','city')

class ServicesStableModel(admin.ModelAdmin):
    list_display = ('stbleHorse','name_Servic', 'duration_service','price')
    list_filter = ('price','duration_service')


class ReviewsAdmin(admin.ModelAdmin):
    list_display=('user','rating','created_at')
    list_filter=('rating',)



admin.site.register(Reviews,ReviewsAdmin)

admin.site.register(StableHorses, StableHorsesModel)

admin.site.register(ServicesStable, ServicesStableModel)


