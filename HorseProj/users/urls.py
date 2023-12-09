from django.urls import path
from . import views

app_name = "users"


urlpatterns = [ 
    path('register/', views.register_views, name="register_views"),
    path('login/',views.login_views,name="login_views"),
    path('logout/', views.logout_views, name="logout_views"),
    path('profile/<user_id>/', views.user_profile_view, name="user_profile_view")
]

