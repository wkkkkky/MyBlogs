# -*- coding: utf-8 -*-
from django import forms
from .models import User


# Profile的表单类
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['link', 'avatar']
