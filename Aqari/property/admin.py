from django.contrib import admin
from .models import Property,Rental,Sale,Comment
# Register your models here.
admin.site.register(Property)
admin.site.register(Rental)
admin.site.register(Sale)
admin.site.register(Comment)
