from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# 用pillow、django-imagekit模块设置图片，可以处理图片，生成指定大小的缩略图，前端显示src="{{ user.avatar.url }}
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# 扩展Django自带的User模型字
class User(AbstractUser):
    nickname = models.CharField(max_length=30, blank=True, null=True, verbose_name='昵称')
    # 扩展用户个人网站字段
    link = models.URLField('个人网址', blank=True, help_text='提示：网址必须填写以http开头的完整形式')
    # 扩展用户头像字段,upload_to后必须是相对路径,上传路径已设置为media，因此upto不需要media/avatar，数据库中avatar/...,前端用avatar.url为media/avatar/...
    avatar = ProcessedImageField(upload_to='avatar', default='avatar/default.png', verbose_name='头像',
                                 processors=[ResizeToFill(100, 100)],  # 处理后的图像大小
                                 format='JPEG',  # 处理后的图片格式
                                 options={'quality': 95}  # 处理后的图片质量
                                 )

    # 重写User的save()方法保存上传的头像目录
    def save(self, *args, **kwargs):
        # 当用户更改头像的时候，avatar.name = '文件名'，其他情况下avatar.name = 'upload_to/文件名'
        if len(self.avatar.name.split('/')) == 1:
            self.avatar.name = self.username + '/' + self.avatar.name
        # 调用父类的save()方法后，avatar.name就变成了'upload_to/用户名/文件名'
        super(User, self).save()

    # 定义网站管理后台表名
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name  # 指定模型的复数形式是什么,如果不指定Django会自动在模型名称后加一个’s’
        ordering = ['-id']
        # admin后台显示名字关联到此表的字段的后天显示名字

    def __str__(self):
        return self.username
