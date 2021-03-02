# -*- coding: utf-8 -*-
from django.urls import path
from .views import profile_view, change_profile_view
from . import views

app_name = 'myaccount'

urlpatterns = [
    # 用户信息
    path('profile/', profile_view, name='profile'),
    path('profile/change/', change_profile_view, name='change_profile'),

]