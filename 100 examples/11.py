
total = 0
a = int(input("please input the month you want:"))
def fib(n):
    if n==1:
        return [1]
    if n==2:
        return[1,1]
    fibs = [1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs
L=fib(a)
print(L)
a =len(L)
#for i in range(0,a):
#    total = total+L(i)
total = total+sum(L)
print(2*total)
'''
a1 = 1
b2 = 1
for i in range(1,12):
    print('%12ld%12ld'%(a1,b2))
    if(i %3)==0:
        print(" ")
    a1 = a1+b2
    b2 = a1+b2
'''