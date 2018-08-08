#------------------------------------
#斐波拉切数列
#数列构成原理,f1=1,f2=1,后面的元素为前两个元素的和
#------------------------------------
n = int(input("请输入一个上限 n:\n"))
def fib(n):
    if n ==1:
        return [1]
    if n ==2:
        return [1,1]
    fibs = [1,1]
    for i in range(2, n):
        fibs.append(fibs[-1]+fibs[-2]) #第3个元素为fibs[0]+fibs[1],
        # 后面的元素为前两个元素和,以此类推
    return fibs
L=fib(n)
print(L)