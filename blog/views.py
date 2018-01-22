from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, InvalidPage
from .models import Post, Tag


def index(request):
    """
    :return: 返回分页对象在模版分页
    """
    post_list = Post.objects.order_by('-created').all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 1)

    try:
        posts = paginator.page(page)
    except InvalidPage:
        # 页码有错误直接返回第1页
        posts = paginator.page(1)

    return render(request, 'index.html', {'posts': posts})


def post(request, post_id):
    blog = get_object_or_404(Post, id=int(post_id))
    context = {
        'blog': blog,
    }
    return render(request, 'post.html', context)
