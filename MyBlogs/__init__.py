import os
from django.apps import AppConfig

VERBOSE_APP_NAME = u"博客管理"
default_app_config = 'MyBlogs.AppVerboseNameConfig'


def get_current_app_name(file):
    return os.path.split(os.path.dirname(file))[-1]


class AppVerboseNameConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME
