# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: urls.py
# Author: L.H
# Time: 2018年01月02日 23:16
# Description:
"""定义pizzeria的URL模式"""
from django.urls import path

from . import views

app_name = '[pizzeria]'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 显示所有pizza
    path('pizzas/', views.pizzas, name='pizzas'),
    path('pizzas/<pizza_id>/', views.pizza, name='pizza'),
]