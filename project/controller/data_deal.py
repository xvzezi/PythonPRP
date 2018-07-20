#-*- coding:utf-8 -*-
import sys
sys.path.append('controller/tool/spider')
from spider import spider
from studentApp import get_and_post

def data_deal(request_from_manager):#request_from_manager是从manager.py接受到的命令
    list1=[]#最终返回给model类一个存放各个data实例的列表
    list2=[]#从model类返回给manager的列表
    if(request_from_manager != "post"):
        list1 = get_data_from_page(request_from_manager)
        if list1 == False:
            return False
        save_data(list1)
        return True
    else:
        list2 = get_data_from_model()

        #处理one_direction, another_direction两项
        if list2 != []:
            for student in list2:
                tmp = [a,b,c,d]
                a = student.a_group.split(',')
                b = student.b_group.split(',')
                c = student.c_group.split(',')
                d = student.d_group.split(',')
                for group in tmp:
                    if int(group[2]) + int(group[3]) >= int(group[1]):
                        student.one_direction = group[0]
                    elif int(group[2]) + int(group[3]) >= 6:
                        student.another_direction = group[0]

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
    def change(self):
        tmp = {'SE112':se112, 'SE418':se418, 'SE419':se419, 'SE420':se420, 'SE422':se422, 'SE114':se114, 'SE113':se113, 'SE232':se232}
        se112 = se418 = se419 = se420 = se422 = se114 = se113 = se232 = '未选课'
        tmplist1 = ['SE112', 'SE418', 'SE419', 'SE420', 'SE422', 'SE114', 'SE113', 'SE232']
        tmplist2 = self.others.split(';')
        for i in tmplist2:
            i = i.split(',')
            for j in tmplist1:
                if j in i[0]:
                    if 'P' in i[2]:
                        tmp[j] = '通过'
                        break
                    if 'F' in i[2]:
                        tmp[j] = '未通过'
                        break
                    if int(i[2]) >= 60:
                        tmp[j] = '通过'
                    else:
                        tmp[j] = '未通过'
        self.others = tmp

def get_data_from_page(re):#根据命令对网页进行爬取并获取数据(re是一个包含用户名和密码的字典)
    #spider.spider(re['username'],re['password'])#spider还在完善中
    return list1
    
def save_data(list1):#将list中的内容传给数据库
    get_and_post.add(list1)
    return

def get_data_from_model():#从model获取数据
    tmp = get_and_post.show()
    list2 = []
    if tmp != []:
        for person in tmp:
            student = data2(person.student_ID, person.name, person.department, person.major, person.grade,
                            person.graduate_time, person.student_status, person.failed_number, person.center_credits,
                            person.courses_must_to_take, person.a_group, person.b_group, person.c_group, person.d_group,
                            person.professional_elective_courses, person.enterprise_education_courses,
                            person.general_courses, person.others, '无', '无')
            student.change()
            list2.append(student)
    return list2
