#----------------------------------------------------------
#写代码，有如下列表，请按照功能要求实现每一个功能
#li = ["hello",'seven',["mon",["h","kelly"],'all'],123,446]
#a.请输出"Kelly"
#b.请使用索引找到 'all'元素并将其修改为"ALL"
#2018-8-19
#----------------------------------------------------------
'''
li = ["hello",'seven',["mon",["h","kelly"],'all'],123,446]
a = li[2][1][1]
print(a.capitalize)
li[2][2] ='ALL'
print(li)
'''
li = ["hello",'seven',["mon",["h","kelly"],'all'],123,446]
print(li[2][1][1].capitalize()) #capitalize用于返回字符串的副本,并将第一个字符大写
index = li[2].index('all') #检测字符串中是否包含子字符串 str,如果包含子字符串返回开始的索引值
li[2][index] = 'ALL'
print(li)






