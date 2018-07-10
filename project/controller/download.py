#-*- coding:utf-8 -*-
import xlsxwriter
def download(list_model,used_class_number):#通过数据对本地的Excel文件进行更改
    #创建一个Excel文件
    workbook = xlsxwriter.Workbook('file.xlsx')
    #创建一个工作表sheet对象
    worksheet = workbook.add_worksheet()
    #向单元格写入数据
    row = list_model[0]   #行数
    column = used_class_number  #列数
    for i in xrange(row):
        for j in xrange(column):
            word_list = ['A','B','C','D','E','F','G','H'
                        'I','J','K','L','M','N','O','P'
                        ,'Q','R','S','T','U','V','W','X',
                        'Y','Z']
            if j <= 26:
                x = word_list[j-1]
            else:
                x = 'A'+word_list[j%26 - 1]
            y = str(i+1)
            data = str(list_show[i+1][j]).decode('utf-8')
            print data
            worksheet.write(x+y,u'%s'%(data))
    #关闭并保存文件
    workbook.close()
    return