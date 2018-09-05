#-----------------------------------------------------
#有两个序列a,b，大小都为n,序列元素的值任意整形数，无序；
#要求：通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最小。
#2018-8-17
#-----------------------------------------------------

str_n1 =input("please input a list:\n")
a = [int(m) for m in str_n1.split()]
str_n2 =input("please input a list:\n")
b = [int(m) for m in str_n2.split()]
x = y =0
min = abs((sum(a) - sum(b)))
tag = 1
while tag :
    old =min
    while x < len(a):
        while y < len(b):
            a[x], b[y] = b[y], a[x]
            print(a)
            print(b)

            tmp = abs((sum(a)-sum(b)))
            if min > tmp:
                min = tmp
            else:
                a[x], b[y] = b[y],a[x]
            print(tmp)
            y = y+1
        x = x+1
        y = 0
    if min == old:
        tag = 0
    else:
        x = y =0
print(min)
print(a)
print(b)
'''

def mindistance(a,b):
    sum1 = sum(a)
    sum2 = sum(b)
    diff = sum1 - sum2
    mini, minj, best = 0, 0, 0
    while (diff!=0):
        for i in range(len(a)):
            for j in range(len(b)):
                if abs(diff - 2*(a[i]-b[j]))<abs(diff -2 *best):
                    best = a[i] - b[j]
                    mini, minj = i,j
        if best ==0:
            return False
        a[mini], b[minj] = b[minj], a[mini]
        sum1 -= best
        sum2 +=best
        diff =sum1 - sum2
    return a,b,diff
str_n1 =input("please input a list:\n")
a = [int(m) for m in str_n1.split()]
str_n2 =input("please input a list:\n")
b = [int(m) for m in str_n2.split()]
print(a)
print(mindistance(a,b))
'''




