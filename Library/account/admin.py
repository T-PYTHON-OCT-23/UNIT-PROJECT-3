from django.contrib import admin
from .models import Profile

# Register your models here.



class ProfileModel(admin.ModelAdmin):

    list_display = ('user', 'is_writer')
    list_filter = ('is_writer',)

admin.site.register(Profile,ProfileModel)

