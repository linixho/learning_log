# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: forms.py
# Author: L.H
# Time: 2018年01月03日 22:40
# Description:
from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic  # 以Topic为模型创建表单
        fields = ['text']  # 表单包含字段text
        labels = {'text': ''}  # ''表示不为text字段生成标签


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
