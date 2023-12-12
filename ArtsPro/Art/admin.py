from django.contrib import admin
from .models import Art , Review

# Register your models here.
class artAdmin(admin.ModelAdmin):
    list_display = ('title' , 'poster')


class ReviewModel(admin.ModelAdmin):
    list_display = ('art' , 'user' , 'comment' ,'created_at')


admin.site.register(Art, artAdmin)
admin.site.register(Review, ReviewModel)


