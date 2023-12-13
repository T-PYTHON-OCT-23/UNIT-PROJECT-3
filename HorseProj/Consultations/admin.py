from django.contrib import admin
from .models import consultation , consultationRequest
# Register your models here.

class consultationModel(admin.ModelAdmin):
    list_display = ('user','category', 'age_horse','horse_type')
    list_filter = ('category',)

class consultationRequestAdmin(admin.ModelAdmin):
    list_display=('user','created_at')

admin.site.register(consultation, consultationModel)
admin.site.register(consultationRequest,consultationRequestAdmin)