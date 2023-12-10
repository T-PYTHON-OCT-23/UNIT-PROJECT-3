from django.contrib import admin
from .models import Product, Review


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'content', 'size','choose_product')
    #list_filter = ('content', 'size')


class ReviewModel(admin.ModelAdmin):
    list_display = ('product','user','rating', 'comment','created_at')
    #list_filter = ('product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewModel)
