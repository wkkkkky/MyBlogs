import markdown
from django import template
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from comment.models import Comment

register = template.Library()  # 自定义filter时必须加上


# 对文章进行markdown格式渲染
@register.filter()
def mard(value):
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),
    ])
    value = md.convert(value)
    return value


# 获取文章的评论数目
@register.filter()
def get_comment_number(value):
    value = Comment.objects.filter(article_id=value).count()
    return value
