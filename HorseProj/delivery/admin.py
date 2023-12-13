from django.contrib import admin
from .models import Store,Menu, MenuRequest
# Register your models here.


class StoreModel(admin.ModelAdmin):
    list_display = ('name','location', 'work_time','rating')
    list_filter = ('rating',)


class MenuModel(admin.ModelAdmin):
    list_display = ('name','description','price')
    list_filter = ('price',)



class MenuRequestAdmin(admin.ModelAdmin):
    list_display=('user', 'menu')

admin.site.register(Menu, MenuModel)

admin.site.register(Store, StoreModel)

admin.site.register(MenuRequest,MenuRequestAdmin)



