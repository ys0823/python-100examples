#--------------------------------------
#求一个区间之前的素数,并分别打印出来
#2018-8-11
#--------------------------------------
import math
m =int(input("请输入一个区间上限值:\n"))
n = int(input("请输入一个区间下限值:\n"))
for i in range(n,m+1):
    leap = 0
    for j in range(2,int(math.sqrt(i))+1):
        if i%j ==0:
            leap =1
            break
    if leap ==0:
        print(i)