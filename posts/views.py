from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime

from posts.forms import PostForm
from posts.models import Post


@login_required
def list_posts(request):
    posts = Post.objects.all().order_by('created')
    context = dict(
        posts=posts
    )
    return render(request, 'posts/feed.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(
        request=request,
        template_name='posts/new.html',
        context=dict(
            form=form,
            user=request.user,
            profile=request.user.profile
        )
    )
