#-------------------------------------
#提问：求1+2!+3!+...+20!的和
#2018-8-8
#-------------------------------------
n = int(input('请输入一个数n:\n'))
s,total = 1,0
for i in range(1,n+1):
    for m in range(1,i+1):
        s = s*m
    t = s
    total = total+t
    s = 1
print(total)