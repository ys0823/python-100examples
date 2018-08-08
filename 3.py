#-----------------------------------
#简述：一个整数，它加上100和加上268后都是一个完全平方数
#提问：请问该数是多少？
#Python解题思路分析：在10000以内判断，将该数加上100后再开方，加上268后再开方，
# 如果开方后的结果满足如下条件，即是结果,Python完全平方数.
#-----------------------------------
import math
#错误解法:math.sqrt()函数的返回值始终是float型,则不能用ininstance判断
'''
for i in range(10000):
    print(i)
    if isinstance(a,int) and isinstance(b,int):
        print(i)
'''
for i in range(10000):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+268))
    if (x*x == i+100) and (y*y == i+268):
        print(i)
