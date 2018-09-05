#--------------------------------------------------------------
#题目：纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
#[
#[1, 82, 65535],
#[20, 90, 13],
#[26, 809, 1024]
#]
#请将上述内容写到 numbers.xls 文件中
#2018-8-23
#--------------------------------------------------------------
import xlwt
with open('E:\\叶盛\\研究生学习\\python\\100 例\\64\\number.txt','r') as f:
    st_name = eval(f.read().strip().replace('\n','')) #读完文件后转成列表
workbook = xlwt.Workbook(encoding = 'ascii')#设置编码
worksheet = workbook.add_sheet('My Worksheet') #创建一个worksheet
for i in range(len(st_name)):
    for j in range(len(st_name[i])):
        worksheet.write(i, j, label = st_name[i][j]) #将行列值写入表格
workbook.save('number.xls') #保存