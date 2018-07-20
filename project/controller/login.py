# -*- coding: utf-8 -*-
from studentApp import models
from django.shortcuts import render
from controller import manager

def login(request):
    if request.method == "POST":
        form = models.UserLogin(request.POST)
        if form.is_valid(): #获取表单信息
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            flg = manager.get_model({'username':username, 'password':password})
            if flg :
                data = manager.return_model("post")
                return render(request, 'index.html', {'x': 1, 'warning': "点击以上按钮即可显示、下载或更新审核结果",'data': data})
        return render(request, 'login.html', {'warning': "用户名或密码不正确"})
    return render(request, 'login.html', {'warning': ""})