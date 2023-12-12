from django.contrib import admin
from .models import Profile, Appointment

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'about')


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('clinic', 'user')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Appointment, AppointmentAdmin)
