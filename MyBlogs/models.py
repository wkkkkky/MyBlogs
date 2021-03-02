from django.db import models
from django.urls import reverse
from mdeditor.fields import MDTextField


# Create your models here.

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
    watch_number = models.PositiveIntegerField(default=0, verbose_name="观看数")
    tag = models.ManyToManyField(Tag, verbose_name="博客标签")
    is_valid = models.BooleanField(default=True)

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

    # 获取文章地址
    def get_absolute_url(self):
        return reverse('article', args=[self.id])
