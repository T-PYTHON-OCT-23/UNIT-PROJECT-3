from django.urls import path
from . import views

app_name = "books"

urlpatterns =[
    path("", views.book_home, name="book_home"),
    path("add/",views.add_book_view, name="add_book_view"),
    path("detail/<book_id>/",views.book_detail_view,name="book_detail_view"),
    path('search/',views.search,name='search'),
    path("update/<book_id>/", views.update, name="update"),
    path('delete/<book_id>/',views.delete,name='delete'),
    path("review/add/<book_id>/", views.add_review_view, name="add_review_view"),
    path("cat/", views.bookCat, name="bookCat"),

]