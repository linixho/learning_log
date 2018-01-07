# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: urls.py
# Author: L.H
# Time: 2018年01月01日 22:29
# Description:
"""定义learning_logs的URL模式"""
from django.urls import path

from . import views

# 下行解决：Specifying a namespace in include() without providing an app_name和XXX is not a registered namespace问题
app_name = '[learning_logs]'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 显示所有的主题
    path('topics/', views.topics, name='topics'),
    path('topics/<topic_id>/', views.topic, name='topic'),

    # 用于添加新主题的网页
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),

    # 用于编辑条目的页面
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
]
