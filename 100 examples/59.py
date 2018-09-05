#-------------------------------------------------------------
#题目：对字典进行有序排序，分别根据字典key或者字典value。
#举例：字典 dd = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
#2018-8-21
#--------------------------------------------------------------
'''
dd = {'banana':3, 'apple':4, 'pear':1, 'orange':2}
sorted_dd1 = sorted(dd.items(), key=lambda x:x[0],reverse=True)
print(sorted_dd1)
sorted_dd2 = sorted(dd.items(), key=lambda x:x[1],reverse=True)
print(sorted_dd2)
'''
import collections
dd = {'banana':3, 'apple':4, 'pear':1, 'orange':2}
sorted_dd1 = collections.OrderedDict(sorted(dd.items(), key=lambda x:x[0],reverse=True))
print(sorted_dd1)
