# myredditapp/urls.py

from django.urls import path
from . import views

app_name = 'Fourm'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:post_id>/upvote/', views.upvote_post, name='upvote_post'),
    path('comment/<int:comment_id>/upvote/', views.upvote_comment, name='upvote_comment'),
    # Add other paths as needed
]
