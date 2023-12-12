from django.urls import path
from . import views

app_name = 'subreddit'

urlpatterns = [
    
    path('post/<subreddit_slug>/create/', views.post_create, name='post_create'),
    path('post/<post_slug>/delete/', views.post_delete, name='post_delete'),
    path('post/<post_slug>/update/', views.post_update, name='post_update'),

    path('view/<subreddit_slug>/', views.subreddit_detail, name='subreddit_detail'),
    path('create/', views.subreddit_create, name='subreddit_create'),
    path('<subreddit_slug>/delete/', views.subreddit_delete, name='subreddit_delete'),
    path('<subreddit_slug>/update/', views.subreddit_update, name='subreddit_update'),

    path('comment/<comment_slug>/delete/', views.comment_delete, name='comment_delete'),
    path('comment/<comment_slug>/update/', views.comment_update, name='comment_update'),
    path('comment/<comment_slug>/reply/', views.comment_reply, name='comment_reply'),
    path('comment/<comment_slug>/detail/', views.comment_detail, name='comment_detail'),
    
]