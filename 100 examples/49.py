#---------------------------------------
#将字符串："k:1|k1:2|k2:3|k3:4"，处理成 python
#字典：{'k':'1', 'k1':'2', 'k2':'3','k3':'4' }
#1018-8-16
#---------------------------------------

s = 'k:1|k1:2|k2:3|k3:4'
s1 = s.split("|")
print(s1)
d1 = {}
a = []
for i in range(0,len(s1)):
    a.append((s1[i]).split(":"))
for i in a:
    d1[i[0]] = i[1]
print(d1)
'''
#参考答案
str1 ='k:1|k1:2|k2:3|k3:4'
str_list =str1.split('|')
d = {}
for l in str_list:
    key,value = l.split(':')
    d[key] = value
print(d)
'''


