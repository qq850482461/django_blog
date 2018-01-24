from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, InvalidPage
from .models import Post, Tag


def index(request):
    """
    主页
    posts返回分页对象在模版分页
    """
    # 根据创建时间倒序排序
    post_list = Post.objects.order_by('-created').all()
    page = request.GET.get('page', 1)
    # 进行分页
    paginator = Paginator(post_list, 5)

    try:
        posts = paginator.page(page)
    except InvalidPage:
        # 页码有错误直接返回第1页
        posts = paginator.page(1)

    return render(request, 'index.html', {'posts': posts})


def post(request, post_id):
    """
    文章详细
    post_id: 文章的主键id
    previous_post : 当前文章的上一篇
    next_post : 当前文章的下一篇
    """
    blog = get_object_or_404(Post, id=int(post_id))
    previous_post = Post.objects.filter(id__lt=int(blog.id)).last()
    next_post = Post.objects.filter(id__gt=int(blog.id)).first()

    context = {
        'blog': blog,
        'previous_post': previous_post,
        'next_post': next_post
    }
    return render(request, 'post.html', context)


def tag(request, tag_name=None):
    """
    标签页
    tag_name: tag字符串
    'tag_name'传入就返回这个tag的所有文章,没有传入就展示所有的标签名字
    """
    if tag_name is None:
        tag_flag = True
        tags = Tag.objects.all()
        return render(request, 'tag.html', context={'tags': tags, 'tag_flag': tag_flag})
    else:
        tag_flag = False
        tag = get_object_or_404(Tag, name=str(tag_name))
        posts = tag.post_set.order_by('-created').all()
        return render(request, 'tag.html', context={'posts': posts, 'tag_flag': tag_flag, 'tag': tag})


def archives(request):
    return render(request, 'archives.html')
