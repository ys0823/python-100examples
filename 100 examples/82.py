#-------------------------------------------
#题目：要求写一个程序，需要用户输入姓名和年龄，然后返回一个时间，告诉用户那一年他会到85岁。
#追加：输入需要追加发送消息的数量，然后打印
#2018-8-30
#-------------------------------------------
import datetime
name = input('please input the name:\n')
age = int(input('please input the age:\n'))
birth_year = datetime.datetime.now().year- age
age_85 = birth_year + 85
print('%s,%d年,你将85岁'%(name,age_85))
