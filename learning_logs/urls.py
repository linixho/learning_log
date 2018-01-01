# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: urls.py
# Author: L.H
# Time: 2018年01月01日 22:29
# Description:
"""定义learning_logs的URL模式"""
from django.urls import path

from . import views

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
]
