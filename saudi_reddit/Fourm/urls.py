# myredditapp/urls.py

from django.urls import path
from . import views

app_name = 'Fourm'

urlpatterns = [
    path('', views.index, name='index'),
    path('<subreddit_slug>/post/<post_slug>/', views.post_detail, name='post_detail'),
    path('<subreddit_slug>/', views.redirectToSub, name='redirectToSub'),
    path('post/<post_slug>/comment/', views.add_comment, name='add_comment'),
    path('post/<post_slug>/upvote/', views.upvote_post, name='upvote_post'),
    path('post/<post_slug>/downvote/', views.downvote_post, name='downvote_post'),
    path('post/<post_slug>/delete/', views.delete_post, name='delete_post'),
    path('comment/<post_slug>/edit/', views.update_comment, name='update_comment'),
    path('comment/<comment_slug>/upvote/', views.upvote_comment, name='upvote_comment'),
    path('comment/<comment_slug>/downvote/', views.downvote_comment, name='downvote_comment'),
    path('comment/<comment_slug>/delete/', views.delete_comment, name='delete_comment'),
    path('home/myfeed',views.Feed,name='Feed'),
    path('search/result', views.Search_bar, name='Search_bar')
    # Add other paths as needed
]
