from django.contrib import admin
from .models import Book,Review
# Register your models here.

class BookAdmin(admin.ModelAdmin):

    list_display = ('name', 'release_date', 'category')
    list_filter = ('category',)

admin.site.register(Book, BookAdmin)

class ReviewModel(admin.ModelAdmin):

    list_display = ('user', 'book', 'comment', 'created_at')
    list_filter = ('book',)

admin.site.register(Review, ReviewModel)