from django.urls import path
from . import views

app_name = 'evalhub'

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('feedback/<int:task_id>/', views.feedback_detail, name='feedback_detail'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
]
