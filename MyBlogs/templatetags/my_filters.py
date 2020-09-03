import markdown
from django import template
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify

register = template.Library()  # 自定义filter时必须加上


@register.filter()
def mard(value):
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),
    ])
    value = md.convert(value)
    return value
