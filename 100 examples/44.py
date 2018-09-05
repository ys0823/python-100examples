#------------------------------------------
#随意输入十个整数，不用sort对输入的十个整数进行从小到大排序排序：
#2018-8-14
#------------------------------------------
str_n =input("please input a list:\n")
n = [int(m) for m in str_n.split()]
print(n)
l = len(n)
for i in range(0,l):
    for j in range(i+1,l):
        if n[j] < n[i]:
            n[j], n[i] = n[i], n[j]
print(n)


