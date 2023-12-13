from django.contrib import admin
from .models import Car , Rental,Review

# Register your models here.

admin.site.register(Car)
admin.site.register(Rental)
admin.site.register(Review)

