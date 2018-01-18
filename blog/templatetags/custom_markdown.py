import markdown2
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

# 自定义filter时必须加上
register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(value):
    """
    自定义一个字符串模版过滤器,
    markdown开启附加功能,
    https://github.com/trentm/python-markdown2/wiki/Extras
    """
    return mark_safe(markdown2.markdown(value, extras=["code-friendly", 'fenced-code-blocks']))
