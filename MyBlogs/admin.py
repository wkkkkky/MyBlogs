from django.contrib import admin
from .models import *


# Register your models here.

# 博客模块
@admin.register(Article)
class BlogsAdmin(admin.ModelAdmin):
    Article.sum_profile.short_description = '博客摘要'
    Article.con_profile.short_description = '博客内容'
    filter_horizontal = ['tag']  # 给多选增加一个左右添加的框
    list_display = ('id', 'title', 'author', 'category', Article.sum_profile, Article.con_profile,
                    'watch_number', 'create_date', 'update_date', 'is_valid')


# 标签模块
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name',)


# 类别模块
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cname',)



