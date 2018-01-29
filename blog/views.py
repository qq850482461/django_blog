from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, InvalidPage
from .models import Post, Tag, About
import time


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
    """
    归档页面,按所有年份进行排序
    :param request:
    :return:
    """

    this_year = time.strftime('%Y', time.localtime(time.time()))
    # 查询比当前年份小的所有年份数据
    previous_year = Post.objects.filter(created__year__lt=this_year).all()
    # 获得出数据库所有年份int类型列表
    previous_list = [int(i.created.strftime('%Y')) for i in previous_year]
    previous_list.append(int(this_year))

    all_year = list(set(previous_list))
    # 反转列表,倒序排列
    all_year.reverse()
    # 按格式序列化
    data = [{str(i): Post.objects.filter(created__year=i).order_by('-created')} for i in all_year]
    # 所有文章数量
    count = Post.objects.all().count()
    return render(request, 'archives.html', context={'datas': data, 'count': count})


def about(request):
    """
    关于页面
    :param request:
    :return:
    """
    data = About.objects.all().first()
    return render(request, 'about.html', context={'data': data})
