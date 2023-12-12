from django.urls import path
from . import views

app_name = "horses"

urlpatterns = [ 
    path('add/', views.add_stable_views, name="add_stable_views"),
    path('', views.home_stable_view, name="home_stable_view"),
    path('details/<stable_id>', views.stable_details_view,name="stable_details_view"),
    path('delete/<stable_id>',views.delete_stable_views,name="delete_stable_views"),
    path('update/<stable_id>',views.update_stable_views, name="update_stable_views"),
    # path("delete/rev/<review_id>/", views.delete_rev_views ,name="delete_rev_views"),
    path('add/service/<stable_id>', views.add_services_view, name="add_services_view")
    
]

