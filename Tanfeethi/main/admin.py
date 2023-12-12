from django.contrib import admin
from .models import Flight , Reservation ,City

# Register your models here.



admin.site.register(Flight)
admin.site.register(Reservation)
admin.site.register(City)

