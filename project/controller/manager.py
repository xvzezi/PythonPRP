#-*- coding:utf-8 -*-
from data_deal import *
from download import *
#与view的接口需要等登录完善之后补全

def get_model(request_from_view):#接受来自view的命令，开始向数据库中增加数据
    if(data_deal(request_from_view)):
        return 1

def return_model(request_from_view):#接受来自view的命令，从数据库中提取数据交给view
    return data_deal(request_from_view)

def download_model(request_from_view,number):#接受来自view的命令，从数据库中提取数据进行下载
    list_download = get_data_from_model(request_from_view)
    list_download = [len(list_download)]+list_download
    download(list_download,number)
    return True
