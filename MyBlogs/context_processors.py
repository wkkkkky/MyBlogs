"""
设置全局上下文处理器
"""
from django.db.models import Count
from MyBlogs.models import Article
from django.db import connection


# 获取右边栏信息
def getRightInfo(request):
    # 获取分类信息
    r_category = Article.objects.values('category__cname', 'category').annotate(c=Count('*')).order_by('-c')

    # 获取近期文章
    r_recarticle = Article.objects.all().order_by('-created_date')[:3]

    # 获取日期归档信息
    cursor = connection.cursor()
    cursor.execute("select create_date,count('*') from myblogs_article GROUP BY DATE_FORMAT(create_date, '%Y-%m')")
    r_archive = cursor.fetchall()
    return {'r_category': r_category, 'r_recarticle': r_recarticle, 'r_archive': r_archive}
