# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from controller import manager

def index(request):
    x = 1#再修读其他方向门数
    warning = "未登录请先登录"
    data = {}
    return render(request, 'index.html', {'x':x, 'warning':warning, 'data':data})

    