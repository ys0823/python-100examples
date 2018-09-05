#-------------------------------------------------------
#已知有一个已经排好序的数组。要求是，有一个新数据项，要求按原来的规律将它插入数组中
#2018-8-12
#------------------------------------------------------

str_n =input("please input a list:\n")
N = [int(m) for m in str_n.split()]
m = int(input("please input the number which you want insert:\n"))
n = sorted(N)
print(list(n))
l =len(N)
index = l
for i in range(l-1,1,-1):
    if m < n[i] and m >n[i-1]:
        index = i
        print(i)
if index ==1:
    if a[0]>m:
        n.insert(0, m)
        print(n)
    elif a[0]<m:
        n.insert(index, m)
        print(n)
else:
    n.insert(index, m)
    print(n)

'''
#参考代码
if __name__ =="__main__":
    str_a = input("please input a list:\n")
    a = [int(m) for m in str_a.split()]
    a.append('0')
    l = len(a)
    print("original list is:")
    for i in range(l):
        print(a[i])
    number = int(input("insert a new number:\n"))
    end = a[l-2]
    if number >end:
        a[l-1] = number
    else:
        for i in range(l-1):
            if a[i]>number:
                temp1 =a[i]
                a[i] =number
                for j in range(i+1, l): #这里让a[i]和后面的a[i+1]依依次往后排序
                    temp2 = a[j]
                    a[j] = temp1
                    temp1 = temp2
                break
    for i in range(0,l):
        print(a[i])
'''

