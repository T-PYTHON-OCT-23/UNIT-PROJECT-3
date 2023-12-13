from django.urls import path
from . import views


app_name = "Art"

urlpatterns = [

    path("add/",views.add_art_view,  name = "add_art_view"),
    path("",views.art_home_view,name = "art_home_view"),
    path("detail/<art_id>/",views.art_detail_view,name="art_detail_view"),
    path("update/<art_id>/",views.update_art_view,name='update_art_view'),
    path("delete/<art_id>/",views.delete_art_view,name='delete_art_view'),
    path("search/",views.search_results_view,name='search_results_view'),
    path("review/add/<art_id>/",views.add_review_view,name='add_review_view')


            
       ]