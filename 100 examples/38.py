#----------------------------------------
#Python练习题问题如下：
#求一个3*3矩阵对角线元素之和
#2018-8-12
#用numpy实现
#----------------------------------------

import numpy as np
x = np.mat('1,2,3;4,5,6;7,8,9')
#x = np.array((1,2,3),(4,5,6,),(7,8,9))
sum = x[0,0]+x[1,1]+x[2,2]
print(sum)

'''
#参考答案
if __name__ =='__main__':
    a =[]
    sum = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append((float(input("input a number:\n"))))
    for i in range(3):
        sum += a[i][j]
    print(sum)
'''