from django.contrib import admin
from .models import Recipe , Review

# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name' , 'category' ,'published_at' , 'description')

    list_filter = ('name', 'category' , 'published_at'  )



class ReviewAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'recipe', 'date', 'rating' )

    list_filter = ('recipe',  'rating' , 'date')



admin.site.register(Recipe ,RecipeAdmin)
admin.site.register(Review,ReviewAdmin )


