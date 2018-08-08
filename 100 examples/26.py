#---------------------------------------
#问题：要求用递归的方法，求5!阶乘
#Python解题思路分析：
#递归公式：fn=fn_1*4!
#2018-8-8
#---------------------------------------

def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j*fact(j-1)  #递归
    return sum

for i in range(5):
    print('%d !=%d'%(i,fact(i)))