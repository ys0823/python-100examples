#----------------------------------------
#删除list里面的重复元素
#2018-8-15
#----------------------------------------
'''
#法一:直接调用set函数
str_n =input("please input a list:\n")
n = [int(m) for m in str_n.split()]
n1 = set(list(n))
print(n1)
'''
#法二:对数组元素进行比较删除
str_n =input("please input a list:\n")
n = [int(m) for m in str_n.split()]
print(n)
l = len(n)
m = []
for i in range(0,l):
    for j in range(i+1,l):
        if n[j] == n[i]:
            m.append(j)
for k in range(len(m)):
    n.remove(n[k])
print(n)