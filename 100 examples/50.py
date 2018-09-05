#-------------------------------------------------------------
#list 对象 alist [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]，
# 请按 alist 中元素的age 由大到小排序；
#2018-8-16
#-------------------------------------------------------------
L = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
L.sort(key=lambda x:x['age'],reverse=True)
#l = L.sort(key=operator.itemgetter('age'),reverse=True)
print(L)

