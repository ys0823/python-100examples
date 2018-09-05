#------------------------------
#排序问题:先选择一个最小的与第一个元素交换。
#之后以此类推，即用第二个元素与后8个进行比较，并进行交换
#冒泡法:2-18-8-11
#------------------------------

#(一)冒泡法
#时间复杂度:O(n^2)

str_n =input("please input a list:\n")
n = [int(m) for m in str_n.split()]
print(n)
l = len(n)
for i in range(0,l): #排序次数
    for j in range(0,l-i-1):
        if n[j]>n[j+1]:
            n[j],n[j+1] =n[j+1],n[j]
print(n)


#(二)选择法
#时间复杂度:O(n^2)
str_n =input("please input a list:\n")
n = [int(m) for m in str_n.split()]
l =len(n)
for i in range(0,l):
    for j in range(i+1,l):
        if n[j]<n[i]:
            n[i],n[j] =n[j],n[i]#把最小的数放最前面
print(n)

