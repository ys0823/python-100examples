#-------------------------------------
#设n是一任意自然数。若将n的各位数字反向排列所得自然数n1与n相等，
# 则称n为一回文数
#问题描述：一个5位数，判断它是不是回文数。
#2018-8-9
#--------------------------------------
n = input("please input a string:\n")
m = list(reversed(n))
l = len(n)
leap = 0
for i in range(0,l):
    if ord(m[i])-ord(n[i])==0:
        leap =0
    elif(ord(m[i])-ord(n[i]) !=0):
        leap = 1
        break
if leap==0:
    print("它是回文符")
elif leap ==1:
    print("它不是回文符")

'''
#参考答案
#但参考答案比较复杂,不建议参考

def Type(num):
    if not isinstance(num,int):
        return False
    if num<0:
        return False
    numlist=[]
    while num>0:
        numlist.append(num%10)
        num = num/10
    reverselist = numlist[:]
    print(reverselist)
    reverselist.reverse()
    return reverselist==numlist
if __name__=='main':
    print(Type(12345))
    print(Type(1234321))
'''
