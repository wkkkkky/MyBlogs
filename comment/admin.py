from django.contrib import admin
from .models import Comment


# Register your models here.
# 评论模块
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'user', 'parent', 'reply_to', 'created',)
