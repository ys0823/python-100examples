#---------------------------------------------
#题目：使用python写一个插入算法。
#要求：给一个列表，对列表中的元素从小到大排序
#2018-9-2
#插入法排序
#---------------------------------------------
str_n =input("please input a list:\n")
n = [int(m) for m in str_n.split()]
for i in range(1,len(n)):
    if n[i-1] >n[i]:
        t = n[i]
        j = i-1
        while j>= 0 and n[j] > t:
            n[j+1] = n[j]
            j = j-1
            n[j+1] = t
print(n)

