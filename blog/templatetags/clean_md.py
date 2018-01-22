from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import re

# 自定义filter时必须加上
register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def clean_md(value):
    """
    :param value:
    :return: 返回过滤了多数空格和md标签的字符串
    """
    context = value[:200]
    regex = r'[\\\`\*\[\]\#\+\-\!\>]'
    context = re.sub(regex, '', context)
    context = re.sub(r"\s{2,}", " ", context)
    return mark_safe(context)
