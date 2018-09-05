#-------------------------------------------------
#按执行效率从高到低排列：f2、f1和f3。
# 要证明这个答案是对的，你应该知道如何分析自己代码的性能。
# Python中有一个很好的程序分析包，可以满足这个需求。
#cProfile包:性能分析
#支持的API run()
#2018-8-16
#------------------------------------------------
import random
def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in  l1 if i<0.5]
    return [i*i for i in l2]

def f2(lIn):
    l1 = [i for i in lIn if i <0.5]
    l2 =sorted(l1)
    return [i*i for i in l2]

def f3(lIn):
    l1 = [i*i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i <(0.5*0.5)]

import cProfile
lIn = [random.random() for i in range(100000)]
cProfile.run('f1(lIn)')
cProfile.run('f2(lIn)')
cProfile.run('f3(lIn)')