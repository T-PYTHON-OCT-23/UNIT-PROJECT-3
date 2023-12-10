from django.contrib import admin
from .models import Clinic, Review, Contact

# Register your models here.


class ClinicAdmin(admin.ModelAdmin):

    list_display = ('name', 'category', 'location')
    list_filter = ('name', 'category')


class ReviewModel(admin.ModelAdmin):
    list_display = ('full_name', 'Clinic', 'rating', 'comment')
    list_filter = ('Clinic', 'rating')


class ContactModel(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'message')


admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Review, ReviewModel)
admin.site.register(Contact, ContactModel)
