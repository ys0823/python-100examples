#------------------------------
#Python素数计算及输出练习题要求如下：
#简述：区间范围101-200
#要求：判断这个区间内有多少个素数，并逐一输出。
#首先，判断这个数是否是素数，方法：用一个数分别去除2到sqrt(这个数)；
#其结果，能被整除，则表明此数不是素数，反之是素数。
#2018-8-2
#------------------------------
h =0
import math
#n = int(input("please input a number between 101 and 200:\n"))
key = 1
for k in range(101,201):
    m = int(math.sqrt(k)+1)
    for i in range(2,m):
        if k % i ==0:
            key = 1
            break #这里需要beak一下,一旦能有整除的就跳出循环
        else:
            key = 0
    #if key ==1:
        #print("这个数不是素数")
    if key ==0:
        print("%d"%k)
        h=h+1
print(h)
