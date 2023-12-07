from django.urls import path
from . import views

app_name = "horses"

urlpatterns = [ 
    path('add/', views.add_stable_views, name="add_stable_views"),
    path('', views.home_stable_view, name="home_stable_view"),
    path('details/<stable_id>', views.stable_details_view,name="stable_details_view")
    
]

