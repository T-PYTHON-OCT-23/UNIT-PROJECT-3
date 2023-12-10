# Fourm/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from User.models import Profile 
from subreddit.models import Subreddit
from django.db.models import Count
from django.core.exceptions import PermissionDenied



def index(request):
    subscribed_subreddits=""
    top_subreddits=""
    top_posts = Post.objects.all().order_by('-votes')[:5]
    top_posts = [post for post in top_posts if post.votes > 0]
    top_subreddits=Post.objects.values('subreddit').annotate(Count('subreddit')).order_by('-subreddit__count')[:5]
    top_subreddits = [Subreddit.objects.get(pk=subreddit['subreddit']) for subreddit in top_subreddits]
    if request.user.is_authenticated:
        try:
            user =  Profile.objects.get(user=request.user)
            subscribed_subreddits = user.subreddit.all()
            if subscribed_subreddits:
                posts = Post.objects.filter(Subreddit__in=subscribed_subreddits)
            else:
                posts = Post.objects.all()
        except:
            print("User has no profile")
            posts = Post.objects.all()
    else:
        posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts , 'subscribed_subreddits':
        subscribed_subreddits, "top_subreddits": top_subreddits, "top_posts": top_posts})



def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    subreddit = post.subreddit
    comments = Comment.objects.filter(post=post)
    post.views += 1
    post.save()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'subreddit': subreddit})

@login_required
def add_comment(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(content=content, author=request.user, post=post)
    return redirect('Fourm:post_detail', slug=post_slug)
from django.contrib import messages

@login_required
def upvote_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    # Check if the user has already upvoted
    if post.upvoters.filter(id=request.user.id).exists():
        messages.warning(request, "You have already upvoted this post.")
    else:
        post.votes += 1
        post.upvoters.add(request.user)
        post.save()

    return redirect('Fourm:post_detail', post_slug=post.slug)

@login_required
def downvote_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    # Check if the user has already downvoted
    if post.downvoters.filter(id=request.user.id).exists():
        messages.warning(request, "You have already downvoted this post.")
    else:
        post.votes -= 1
        post.downvoters.add(request.user)
        post.save()

    return redirect('Fourm:post_detail', post_slug=post.slug)

@login_required
def upvote_comment(request, comment_slug):
    comment = get_object_or_404(Comment, slug=comment_slug)

    # Check if the user has already upvoted
    if comment.upvoters.filter(id=request.user.id).exists():
        messages.warning(request, "You have already upvoted this comment.")
    else:
        comment.votes += 1
        comment.upvoters.add(request.user)
        comment.save()

    return redirect('Fourm:post_detail', post_slug=comment.post.slug)

@login_required
def downvote_comment(request, comment_slug):
    comment = get_object_or_404(Comment, slug=comment_slug)

    # Check if the user has already downvoted
    if comment.downvoters.filter(id=request.user.id).exists():
        messages.warning(request, "You have already downvoted this comment.")
    else:
        comment.votes -= 1
        comment.downvoters.add(request.user)
        comment.save()

    return redirect('Fourm:post_detail', post_slug=comment.post.slug)


@login_required
def delete_comment(request, comment_slug):
    comment = get_object_or_404(Comment, slug=comment_slug)
    if comment.author == request.user:
        comment.delete()
    else:
        raise PermissionDenied 
    return redirect('Fourm:post_detail', post_slug=comment.post.slug)