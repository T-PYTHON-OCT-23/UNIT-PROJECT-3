from django.urls import path
from . import views

app_name = 'evalhub'

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('feedback/<int:task_id>/', views.feedback_detail, name='feedback_detail'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('register/', views.register_user_view, name='register_user_view'),
    path('login/', views.login_user_view, name='login_user_view'),
    path('logout/', views.logout_user_view, name='logout_user_view'),
    path('profile/', views.user_profile_view, name='user_profile_view'),
    path('update_profile/', views.update_user_view, name='update_user_view'),
]
