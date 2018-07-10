#-*- coding:utf-8 -*-
import sys
sys.path.append('/tool/spider')
from spider import *
from studentApp import get_and_post

def data_deal(request_from_manager):#request_from_manager是从manager.py接受到的命令
    list1=[]#最终返回给model类一个存放各个data实例的列表
    list2=[]#从model类返回给manager的列表
    if():
        list1 = get_data_from_page(request_from_manager)
        save_data(list1)
        return True
    else():
        list2 = get_data_from_model(request_from_manager)

        #处理one_direction, another_direction两项

        return list2


class data1:#生成data实例
    def __init__(self, student_ID, name, department, major, grade, graduate_time, student_status,
                 failed_number, center_credits, courses_must_to_take, a_group, b_group, c_group, d_group,
                 professional_elective_courses, enterprise_education_courses, general_courses, others):
        self.student_ID = student_ID#学号
        self.name = name#姓名
        self.department = department#学院
        self.major = major#专业
        self.grade = grade#年级
        self.graduate_time = graduate_time#毕业时间
        self.student_status = student_status#学籍状态
        self.failed_number = failed_number#不及格门数
        self.center_credits = center_credits#目前修读核心课程学分
        self.courses_must_to_take = courses_must_to_take#暂未修读课程
        self.a_group = a_group
        self.b_group = b_group
        self.c_group = c_group
        self.d_group = d_group
        self.professional_elective_courses = professional_elective_courses#专业选修课
        self.enterprise_education_courses = enterprise_education_courses#企业教育课
        self.general_courses = general_courses#通识及以下栏目
        self.others = others#必修的选修课

class data2(data1):#返回给manager的数据实例
    def __init__(self, student_ID, name, department, major, grade, graduate_time, student_status,
                 failed_number, center_credits, courses_must_to_take, a_group, b_group, c_group, d_group,
                 professional_elective_courses, enterprise_education_courses, general_courses, others,
                 one_direction, another_direction):
        data1.__init__(self,student_ID,name,department,major,grade,graduate_time,student_status,
                 failed_number,center_credits,courses_must_to_take,a_group,b_group,c_group,d_group,
                 professional_elective_courses,enterprise_education_courses,general_courses,others)#原始数据初始化
        self.one_direction = one_direction#修读完某一方向
        self.another_direction = another_direction#再修读其他方向x门（x可设置）


def get_data_from_page(re):#根据命令对网页进行爬取并获取数据
    return list1
    
def save_data(list1):#将list中的内容传给数据库
    get_and_post.add(list1)
    return

def get_data_from_model(re):#从model获取数据
    tmp = get_and_post.show()
    for person in tmp:
        student = data2(person.student_ID, person.name, person.department, person.major, person.grade,
                        person.graduate_time, person.student_status, person.failed_number, person.center_credits,
                        person.courses_must_to_take, person.a_group, person.b_group, person.c_group, person.d_group,
                        person.professional_elective_courses, person.enterprise_education_courses,
                        person.general_courses, person.others, '', '')
        list2.append(student)
    return list2
