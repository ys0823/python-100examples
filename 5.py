#-----------------------------------------
#Python练习题问题如下：
#整数顺序排列问题简述：任意三个整数类型，x、y、z
#提问：要求把这三个数，按照由小到大的顺序输出
#Python解题思路分析：
#首先，要想方法把最小的数放到x位上，之后将x与y进行比较；
#如果x>y的话，就将x与y的值进行交换；
#然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
#------------------------------------------
'''
#我的解题思路
a = int(input("please input number one:\n"))
b = int(input("please input number two:\n"))
c = int(input("please input number three:\n"))
if b>a:
    lamda = a
    a = b
    b = lamda
    if c>a:
        lamda = a
        a = c
        c = lamda
print("%d%d%d"%(c,b,a))
'''

#参考答案
l = []
for i in range(3): #控制输入的是3个数
    x = int(input("integer:\n"))
    l.append(x)
l.sort() #sort用法可以直接将list里面的元素从小到大排列
print(l)