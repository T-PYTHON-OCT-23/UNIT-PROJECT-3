from django.urls import path
from . import views

app_name = "horses"

urlpatterns = [ 
    path('add/', views.add_stable_views, name="add_stable_views"),
    path('', views.home_stable_view, name="home_stable_view"),
    path('details/<stable_id>', views.stable_details_view,name="stable_details_view"),
    path('delete/<stable_id>',views.delete_stable_views,name="delete_stable_views"),
    path('update/<stable_id>',views.update_stable_views, name="update_stable_views"),
    path('add/service/<stable_id>', views.add_services_view, name="add_services_view"),
    path('search', views.search_horses_view , name="search_horses_view"),
    path('add/request/<service_id>', views.add_stable_request_view, name="add_stable_request_view"),
    path('myRequest/', views.stable_request_view, name="stable_request_view")

    
]

