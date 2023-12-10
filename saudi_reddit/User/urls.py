from django.urls import path, include
from . import views

app_name = 'User'

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # Add signup view
    path('login/', views.user_login, name='login'),  # Add login view
    path('logout/', views.user_logout, name='logout'),  # Add logout view
    path('<username>/', views.profile_Data, name='profile_with_username'),  # Add profile view
    path('profile/edit/', views.edit_profile, name='edit_profile'),  # Add edit profile view
]