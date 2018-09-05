#--------------------------------------------------
#纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

#{
#"1":["张三",150,120,100],
#"2":["李四",90,99,95],
#"3":["王五",60,66,68]
#}

#请将上述内容写到 student.xls 文件中
#2018-8-28
#---------------------------------------------------
import xlwt,json
from collections import OrderedDict

with open('E:\\叶盛\\研究生学习\\python\\100 例\\75\\student.txt','r') as f:
    data = json.load(f, object_pairs_hook = OrderedDict)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('student', cell_overwrite_ok=True) #创建一个worksheet
    for index,(key,values) in enumerate(data.items()):
        sheet1.write(index, 0 ,key)
        for i, value in enumerate(values):
            sheet1.write(index, i+1 ,value)
    workbook.save('E:\\叶盛\\研究生学习\\python\\100 例\\75\\number.xls') #保存