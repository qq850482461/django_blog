from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    """
    标签模型
    """
    name = models.CharField('标签名', max_length=20)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<TAG:{0}>'.format(self.id)


class Post(models.Model):
    """
    文章模型
    '子表'添加外键关联'父表'
    """
    title = models.CharField('标题', max_length=20)
    content = models.TextField('内容')
    created = models.DateTimeField(auto_now_add=True)

    # 关联'User父表',一对多关系
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 关联'Tag',多对多关系(这里名称不能用小写的类名),允许为空,系统会自动添加一张辅助表
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title

    def __repr__(self):
        return '<Post:{0}>'.format(self.id)
