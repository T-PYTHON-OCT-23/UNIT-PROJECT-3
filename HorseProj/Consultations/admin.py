from django.contrib import admin
from .models import consultation
# Register your models here.

class consultationModel(admin.ModelAdmin):
    list_display = ('user','category', 'age_horse','horse_type')
    list_filter = ('category',)

admin.site.register(consultation, consultationModel)