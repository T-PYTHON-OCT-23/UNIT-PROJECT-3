from django.urls import path
from . import views

app_name ='users'

urlpatterns = [
    path('logup/',views.logup_view,name='logup_view'),
    path('login/',views.login_view,name='login_view'),
    path('logout/',views.logout_view,name='logout_view'),
    path('profile/<user_id>/',views.profile_view,name='profile_view'),
    path('update/profile/',views.update_profile_view,name='update_profile_view')
    
]