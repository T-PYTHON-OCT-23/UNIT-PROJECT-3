from django.shortcuts import render, get_object_or_404, redirect
from .models import Subreddit
from Fourm.models import Post, Comment
from .forms import PostForm, SubredditForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


@login_required
def post_create(request,subreddit_slug):
    
    if request.user not in get_object_or_404(Subreddit, slug=subreddit_slug).subscribers.all():
        return redirect('subreddit:subreddit_detail', subreddit_slug=subreddit_slug)

    if request.method == 'POST':
        
        if request.POST.get('Title') and request.POST.get('Content'):
            post = Post.objects.create(title=request.POST.get('Title'),
                                       content=request.POST.get('Content'), author=request.user,
                                       subreddit = get_object_or_404(Subreddit, slug=subreddit_slug))
            
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')
        if request.FILES.get('video'):
            post.video = request.FILES.get('video')
        post.save()
        return redirect('Fourm:post_detail', subreddit_slug=subreddit_slug , post_slug=post.slug)

    else:
        return render(request, 'post_create.html')

@login_required
def post_delete(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    subreddit = post.subreddit
    if request.user == post.author:
        post.delete()
        return redirect('subreddit:subreddit_detail', subreddit_slug=subreddit.slug) 
    return PermissionDenied

@login_required
def post_update(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    if request.method == 'POST' and request.user == post.author:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('subreddit:post_detail', post_slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_update.html', {'form': form, 'post': post})


def subreddit_detail(request, subreddit_slug):
    subreddit = get_object_or_404(Subreddit, slug=subreddit_slug)
    posts = Post.objects.filter(subreddit=subreddit)
    return render(request, 'subreddit_detail.html', {'subreddit': subreddit, 'posts': posts})

@login_required
def subreddit_create(request):

    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('description'):
            subreddit = Subreddit()
            subreddit.name = request.POST.get('name')
            subreddit.description = request.POST.get('description')
            subreddit.author = request.user
            subreddit.save()
            subreddit.subscribers.add(request.user)
        if request.FILES.get('icon') and request.FILES.get('header'):
            subreddit.icon = request.FILES.get('icon')
            subreddit.header = request.FILES.get('header')
        subreddit.save()
        return redirect('subreddit:subreddit_detail', subreddit_slug=subreddit.slug)
    else:
        return render(request, 'subreddit_create.html')

@login_required
def subreddit_delete(request, subreddit_id):
    subreddit = get_object_or_404(Subreddit, pk=subreddit_id)
    if request.method == 'POST' and request.user == subreddit.creator:
        subreddit.delete()
        return redirect('Fourm:index')  # Redirect to the subreddit list page
    return PermissionDenied

@login_required
def subreddit_update(request, subreddit_slug):
    subreddit = get_object_or_404(Subreddit, subreddit_slug=subreddit_slug)
    if request.user == subreddit.creator:
        if request.method == 'POST':
            subreddit = get_object_or_404(Subreddit, subreddit_slug=subreddit_slug)
            if request.POST.get('name'):
                subreddit.name = request.POST.get('name')
            if request.POST.get('description'):
                subreddit.description = request.POST.get('description')
            if request.FILES.get('icon'):
                subreddit.icon = request.FILES.get('icon')
            if request.FILES.get('header'):
                subreddit.header = request.FILES.get('header')
            subreddit.save()
            return redirect('subreddit:subreddit_detail', subreddit_slug=subreddit_slug)
        else:
            return render(request, 'subreddit_update.html', {'subreddit': subreddit})
    else:
        PermissionDenied
    

@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST' and request.user == comment.author:
        comment.delete()
        return redirect('subreddit:post_detail', post_id=comment.post.id)
    return render(request, 'comment_delete.html', {'comment': comment})

@login_required
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST'  and request.user == comment.author :
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('subreddit:post_detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comment_update.html', {'form': form, 'comment': comment})


@login_required
def comment_reply(request, comment_slug):
    comment = get_object_or_404(Comment, slug=comment_slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent = get_object_or_404(Comment, slug=comment_slug)
            comment.post = comment.parent.post
            comment.save()
            return redirect('subreddit:post_detail', post_id=comment.post.id)
    else:
        form = CommentForm()
    return render(request, 'comment_reply.html', {'form': form, 'comment': comment})


def comment_detail(request, comment_slug):
    comment = get_object_or_404(Comment, slug=comment_slug)
    
    return render(request, 'comment_detail.html', {'comment': comment})


@login_required
def subscribe(request, subreddit_slug):
    subreddit = get_object_or_404(Subreddit, slug=subreddit_slug)
    subreddit.subscribers.add(request.user)
    return redirect('subreddit:subreddit_detail', subreddit_slug=subreddit.slug)

@login_required

def unsubscribe(request, subreddit_slug):
    subreddit = get_object_or_404(Subreddit, slug=subreddit_slug)
    subreddit.subscribers.remove(request.user)
    return redirect('subreddit:subreddit_detail', subreddit_slug=subreddit.slug)