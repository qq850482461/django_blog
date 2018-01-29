from django.contrib import admin
from .models import Post, Tag, About
from .forms import PostForm, AboutForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    重写admin后台的字段,并注册
    """
    form = PostForm


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """
    重写admin后台的字段,并注册
    """
    form = AboutForm


admin.site.register(Tag)
