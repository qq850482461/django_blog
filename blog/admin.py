from django.contrib import admin
from .models import Post, Tag
from .forms import PostForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    重写admin后台的字段,并注册
    """
    form = PostForm


admin.site.register(Tag)
