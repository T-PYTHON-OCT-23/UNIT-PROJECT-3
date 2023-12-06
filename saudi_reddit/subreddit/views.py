from django.shortcuts import render, get_object_or_404, redirect
from .models import Subreddit
from Fourm.models import Post, Comment
from .forms import PostForm, SubredditForm, CommentForm
from django.contrib.auth.decorators import login_required


def post_create(request,subreddit_slug):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = PostForm(request.POST)
            form.instance.author = request.user
            form.instance.subreddit = get_object_or_404(Subreddit, slug=subreddit_slug)
            if request.FILES.get('image'):
                form.instance.image = request.FILES.get('image')
            if request.FILES.get('video'):
                form.instance.video = request.FILES.get('video')
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('post_detail', post_id=post.id)
        else:
            return redirect('User:login')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    subreddit = post.subreddit
    if request.method == 'POST' and request.user == post.author:
        post.delete()
        return redirect('subreddit:home', subreddit_slug=subreddit.slug) 
    return render(request, 'post_delete.html', {'post': post})

@login_required
def post_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST' and request.user == post.author:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_update.html', {'form': form, 'post': post})

@login_required
def subreddit_create(request):
    if request.method == 'POST':
        form = SubredditForm(request.POST)
        if form.is_valid():
            subreddit = form.save()
            return redirect('subreddit_detail', subreddit_slug=subreddit.slug)
    else:
        form = SubredditForm()
    return render(request, 'subreddit_create.html', {'form': form})

@login_required
def subreddit_delete(request, subreddit_id):
    subreddit = get_object_or_404(Subreddit, pk=subreddit_id)
    if request.method == 'POST' and request.user == subreddit.creator:
        subreddit.delete()
        return redirect('subreddit_list')  # Redirect to the subreddit list page
    return render(request, 'subreddit_delete.html', {'subreddit': subreddit})

@login_required
def subreddit_update(request, subreddit_id):
    subreddit = get_object_or_404(Subreddit, pk=subreddit_id)
    if request.method == 'POST'  and request.user == subreddit.creator:
        form = SubredditForm(request.POST, instance=subreddit)
        if form.is_valid():
            form.save()
            return redirect('subreddit_detail', subreddit_id=subreddit.id)
    else:
        form = SubredditForm(instance=subreddit)
    return render(request, 'subreddit_update.html', {'form': form, 'subreddit': subreddit})

@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST' and request.user == comment.author:
        comment.delete()
        return redirect('post_detail', post_id=comment.post.id)
    return render(request, 'comment_delete.html', {'comment': comment})

@login_required
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST'  and request.user == comment.author :
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comment_update.html', {'form': form, 'comment': comment})
