from django.contrib import admin
from .models import Service,ServiceDetails,ServiceRequest
# Register your models here.


admin.site.register(Service)
admin.site.register(ServiceDetails)
admin.site.register(ServiceRequest)