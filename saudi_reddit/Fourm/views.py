# Fourm/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment

def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(Subreddit__in=request.user.profile.subreddit.all())
    else:
        posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})



def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    post.views += 1
    post.save()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(content=content, author=request.user, post=post)
    return redirect('post_detail', post_id=post_id)

@login_required
def upvote_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.votes += 1
    post.save()


@login_required
def upvote_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.votes += 1
    comment.save()
