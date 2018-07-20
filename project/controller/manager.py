#-*- coding:utf-8 -*-
from data_deal import *
from download import *
from django.shortcuts import render
from django.http import StreamingHttpResponse
#与view的接口需要等登录完善之后补全

def get_model(request_from_view):#接受来自view的命令，开始向数据库中增加数据
    if data_deal(request_from_view):
        return 1#获取成功
    else:
        return 0#获取失败

def return_model(request_from_view):#接受来自view的命令，从数据库中提取数据交给view
    return data_deal(request_from_view)

def download_model(request):#接受来自view的命令，从数据库中提取数据进行下载
    number = 22
    list_download = get_data_from_model()
    list_download = [len(list_download)]+list_download
    download(list_download,number)
    def file_iterator(file_name, chunk_size=512):#用于形成二进制数据
        with open(file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    the_file_name ="file.xlsx"#要下载的文件路径
    response =StreamingHttpResponse(file_iterator(the_file_name))#这里创建返回
    response['Content-Type'] = 'application/vnd.ms-excel'#注意格式 
    response['Content-Disposition'] = 'attachment;filename="毕业审核表格.xlsx"'#注意filename 这个是下载后的名字
    return response
