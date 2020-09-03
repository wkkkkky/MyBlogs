from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from fsspec.caching import caches

from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# 将用户登录信息封装到类中，以保存到session
class UserMessage(object):
    def __init__(self, email, pwd):
        self.email = email
        self.pwd = pwd

    def __getstate__(self):
        data = self.__dict__.copy()
        del data['pwd']
        return data


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


# 返回首页，传回分页数据
def index(request):
    page_number = request.GET.get('page', 1)
    blogs = Article.objects.all().order_by('-create_date')
    page_obj, page_list, page = pag(blogs, page_number)
    return render(request, 'index.html', {'page_obj': page_obj, 'page_list': page_list, 'page': page})


# 登录
class LoginView(View):
    @staticmethod
    def get(request):
        # if 'login' in request.COOKIES:
        #     login_cookie = request.get_signed_cookie('login', salt='gawk').split(',')
        #     email = login_cookie[0]
        #     return render(request, 'login.html', {'email': email})
        return render(request, 'login.html')

    @staticmethod
    def post(request):
        email = request.POST.get('login_email', '')
        pwd = request.POST.get('login_password', '')
        # remember = request.POST.get('remember', '')
        password = User.objects.get(email=email).password
        if password and password == pwd:
            return redirect('/')
            # response = HttpResponse()
            # response.status_code = 302
            # response.setdefault('Location', '/')
            # user = UserMessage(email, pwd)
            # request.session['login'] = json.dumps(user.__dict__)
            # if remember == 'remember-me':
            #     response.set_signed_cookie('login', email + ',' + pwd, max_age=3 * 60 * 60 * 24, salt='gawk')
            # return response
        return render(request, 'login.html')


# 注册
def register(request):
    # GET请求，返回注册页面
    if request.method == "GET":
        return render(request, 'register.html')
    # form表单提交POST请求，进行注册处理
    name = request.POST.get('register_name')
    email = request.POST.get('register_email')
    pwd1 = request.POST.get('register_pwd1')
    pwd2 = request.POST.get('register_pwd2')

    if name and email and pwd1 == pwd2:
        user = User(username=name, email=email, password=pwd1)
        user.save()
        return HttpResponse("注册成功")
    else:
        return HttpResponse("密码不一致")


# 博客文章
def article(request, pk):
    blog = Article.objects.get(pk=pk)
    return render(request, 'blog.html', {'blog': blog})


# 实现分类跳转
def r_category(request, category):
    page_number = request.GET.get('page', 1)
    ca_article = Article.objects.filter(category__cname=category)
    page_obj, page_list, page = pag(ca_article, page_number)
    return render(request, 'index.html', {'page_obj': page_obj, 'page_list': page_list, 'page': page})


# 根据日期返回博客，实现归档跳转
def archive(request, year, month):
    page_number = request.GET.get('page', 1)
    ar_article = Article.objects.filter(create_date__year=year, create_date__month=month)
    page_obj, page_list, page = pag(ar_article, page_number)
    return render(request, 'index.html', {'page_obj': page_obj, 'page_list': page_list, 'page': page})
