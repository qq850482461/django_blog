from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    文章模型
    author关联User 一对多
    """
    title = models.CharField('标题', max_length=20)
    content = models.TextField('内容')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title

    def __repr__(self):
        return '<Post:{0}>'.format(self.id)


class Tag(models.Model):
    """
    分类标签模型
    post关联Post 一对多
    """
    name = models.CharField('标签名', max_length=20)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<TAG:{0}>'.format(self.id)
