from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from comment.models import Comment
from comment.forms import CommentForm


# 返回首页，传回分页数据
def index(request):
    page_number = request.GET.get('page', 1)
    blogs = Article.objects.all().order_by('-create_date')
    page_obj, page_list, page = pag(blogs, page_number)
    return render(request, 'MyBlogs/index.html', {'page_obj': page_obj, 'page_list': page_list, 'page': page})


# 博客文章
@cache_page(10)
def article(request, pk):
    blog = Article.objects.get(pk=pk)
    # 获取评论
    comments = Comment.objects.filter(article=pk)
    # 引入评论表单
    comment_form = CommentForm()
    # 获取评论数目
    c_number = Comment.objects.filter(article_id=pk)
    # 浏览量 +1
    blog.watch_number += 1
    blog.save(update_fields=['watch_number'])
    context = {'blog': blog, 'comments': comments, 'c_number': c_number, 'comment_form': comment_form, }
    return render(request, 'MyBlogs/blog.html', context)


# 实现分类跳转
def r_category(request, category):
    page_number = request.GET.get('page', 1)
    ca_article = Article.objects.filter(category__cname=category)
    page_obj, page_list, page = pag(ca_article, page_number)
    return render(request, 'MyBlogs/index.html', {'page_obj': page_obj, 'page_list': page_list, 'page': page})


# 根据日期返回博客，实现归档跳转
def archive(request, year, month):
    page_number = request.GET.get('page', 1)
    ar_article = Article.objects.filter(create_date__year=year, create_date__month=month)
    page_obj, page_list, page = pag(ar_article, page_number)
    return render(request, 'MyBlogs/index.html', {'page_obj': page_obj, 'page_list': page_list, 'page': page})


# 分页功能,传回分页数据，
# page_obj为当前请求页面，
# page为总分页数据，
# page_list为当前页面附近几个页面分页值
def pag(pages, page_number):
    page = Paginator(pages, 2)
    try:
        page_obj = page.get_page(page_number)
    except PageNotAnInteger:
        page_obj = page.get_page(1)
    except EmptyPage:
        page_obj = page.get_page(page.num_pages)

    begin = int(page_number) - 2
    if begin < 1:
        begin = 1
    end = begin + 4
    if end > page.num_pages:
        end = page.num_pages
    if end < 5:
        begin = 1
    else:
        begin = end - 4
    page_list = range(begin, end + 1)

    return page_obj, page_list, page
