from django.db import models
from myaccount.models import User
from MyBlogs.models import Article
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField


# 博文的评论
class Comment(MPTTModel):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    # mptt树形结构
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    # 记录二级评论给谁
    reply_to = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replyers'
    )
    # 使用富文本编辑器
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['created']
        verbose_name_plural = u'评论'

    def __str__(self):
        return self.body[:20]
