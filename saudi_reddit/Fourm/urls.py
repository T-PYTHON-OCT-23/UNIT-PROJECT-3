# myredditapp/urls.py

from django.urls import path
from . import views

app_name = 'Fourm'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<post_slug>/', views.post_detail, name='post_detail'),
    path('post/<post_slug>/comment/', views.add_comment, name='add_comment'),
    path('post/<post_slug>/upvote/', views.upvote_post, name='upvote_post'),
    path('comment/<comment_slug>/upvote/', views.upvote_comment, name='upvote_comment'),
    path('comment/<comment_slug>/downvote/', views.downvote_comment, name='downvote_comment'),
    path('comment/<comment_slug>/delete/', views.delete_comment, name='delete_comment'),
    # Add other paths as needed
]
