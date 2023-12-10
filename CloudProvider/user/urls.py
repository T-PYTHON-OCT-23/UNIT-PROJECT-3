from . import views
from django.urls import path



app_name = 'user'


urlpatterns = [
    path('regisrtation',views.user_create_view,name='user_create_view'),
    path('log/in',views.login_view,name='login_view'),
    path('log/out',views.logout_view,name='logout_view'),
    path('<user_id>/profile/',views.profile_view,name='profile_view'),
    path('<user_id>/profile/edit/',views.edit_profile_view,name='edit_profile_view'),
]
