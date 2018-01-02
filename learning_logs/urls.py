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
]
