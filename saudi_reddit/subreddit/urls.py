from django.urls import path
from . import views

app_name = 'subreddit'

urlpatterns = [
    
    path('post/create/', views.post_create, name='post_create'),
    path('post/<post_slug>/delete/', views.post_delete, name='post_delete'),
    path('post/<post_slug>/update/', views.post_update, name='post_update'),

    path('subreddit/create/', views.subreddit_create, name='subreddit_create'),
    path('subreddit/<subreddit_slug>/delete/', views.subreddit_delete, name='subreddit_delete'),
    path('subreddit/<subreddit_slug>/update/', views.subreddit_update, name='subreddit_update'),

    path('comment/<comment_slug>/delete/', views.comment_delete, name='comment_delete'),
    path('comment/<comment_slug>/update/', views.comment_update, name='comment_update'),
    
]