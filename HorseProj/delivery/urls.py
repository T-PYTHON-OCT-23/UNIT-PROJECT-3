from django.urls import path
from . import views

app_name = "delivery"

urlpatterns = [ 
    path('add/', views.add_store_view, name="add_store_view"),
    path('', views.home_store_view, name="home_store_view"),
    path('details/<store_id>', views.store_details_view,name="store_details_view"),
    path('delete/<store_id>', views.delete_store_views, name="delete_store_views"),
    path('add/menu/<store_id>', views.add_menu_view, name="add_menu_view"),
    path('update/<store_id>',views.update_store_views, name="update_store_views"),
    path('add/request/<menu_id>', views.add_menu_request_view, name="add_menu_request_view"),
    path('myRequest/', views.menu_request_view, name="menu_request_view")
    

    
]