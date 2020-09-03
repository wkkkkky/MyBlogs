from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.
# 用户信息
class User(models.Model):
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return u'%s' % self.username

    class Meta:
        ordering = ['id']
        verbose_name_plural = u'用户'


# 文章标签
class Tag(models.Model):
    tag_name = models.CharField(max_length=30, unique=True, verbose_name='标签')

    def __str__(self):
        return u'%s' % self.tag_name

    class Meta:
        ordering = ['id']
        verbose_name_plural = u'标签'


# 文章类别
class Category(models.Model):
    cname = models.CharField(max_length=30, unique=True, verbose_name='类别')

    def __str__(self):
        return u'%s' % self.cname

    class Meta:
        ordering = ['id']
        verbose_name_plural = u'类别'


# 文章信息
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题", unique=True)
    author = models.CharField(max_length=20, verbose_name="博客作者")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="博客类别")
    summary = models.TextField(max_length=100, verbose_name="博客摘要")
    context = MDTextField(null=True, blank=True, verbose_name="博客内容")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_valid = models.BooleanField(default=True)
    watch_number = models.IntegerField(default=0, verbose_name="观看数")
    tag = models.ManyToManyField(Tag, verbose_name="博客标签")

    class Meta:
        ordering = ['-create_date']
        verbose_name_plural = u'文章'

    def __str__(self):
        return u'Article:%s' % self.title

    def sum_profile(self):
        if len(self.summary) > 10:
            return "{}......".format(self.summary[:10])
        else:
            return self.summary

    def con_profile(self):
        if len(self.context) > 10:
            return "{}......".format(self.context[:10])
        else:
            return self.context


# 文章评论
class Comment(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="评论者")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="文章")
    comment = models.CharField(max_length=300, verbose_name="评论")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % self.comment[:10]

    class Meta:
        ordering = ['-id']
        verbose_name_plural = '评论'

    def profile(self):
        if len(self.comment) > 10:
            return "{}......".format(self.comment[:10])
        else:
            return self.comment
