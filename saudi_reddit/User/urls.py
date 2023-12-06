from django.urls import path, include
from . import views

app_name = 'User'

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # Add signup view
    path('login/', views.login, name='login'),  # Add login view
]