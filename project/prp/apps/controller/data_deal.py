#-*- coding:utf-8 -*-

def main(request_from_manager):#request_from_manager是从manager.py接受到的命令
    list1=[]#最终返回给model类一个存放各个data实例的列表
    list2=[]#从model类返回给manager的列表
    if():
        list1 = get_data_from_page(request_from_manager)
        save_data(list1)
        return []
    else():
        list2 = get_data_from_model(request_from_manager)
        return list2


class data1()#生成data实例
class data2()#返回给manager的数据实例
def get_data_from_page(re):#根据命令对网页进行爬取并获取数据
    return list1
def save_data(list1):#将list中的内容传给数据库
    return
def get_data_from_model(re):#从model获取数据
    return list2