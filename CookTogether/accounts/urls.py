from django.urls import path
from . import views
app_name = "accounts"
urlpatterns = [
       path('register/',views.register_user,name='register_user'),
        path('login/',views.login_page,name='login_page'),
        path('logout/',views.logout_page,name='logout_page')
]
