from django.shortcuts import render, get_object_or_404
from .models import Post, Tag


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)


def post(request, post_id):
    blog = get_object_or_404(Post, id=int(post_id))
    context = {
        'blog': blog,
    }
    return render(request, 'post.html', context)
