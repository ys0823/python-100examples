#--------------------------------------
#问题描述：
#求这样的一组数据和，s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字；
#例如：2+22+222+2222+22222(此时共有5个数相加)，这里具体是由几个数相加，由键盘控制。
#2018-8-4
#--------------------------------------

n =int(input("please input a num: "))
a = int(input("please input a:"))
s = 0
total =0
for i in range(0,n):
    s = s+a*pow(10,i)
    total +=s
print("total is%d"%(total))