#-----------------------------------------------------
#题目：随机生成1到100之间的整数，有六次猜测机会。
#要求：输入六次判断输入的数字是否和随机生成的数字是否相同，
# 如果不同打印是否大于或者小于生成数，六次用完还没才对，打印出生成数。
#2018-8-29
#-----------------------------------------------------
import random
n = random.randint(0,100)
print(n)
leap = 0
L = []
for i in range(0,6):
    m1 = int(input('Please enter the number your guess:\n'))
    L.append(m1)
    if m1 ==n:
        print('Congratulations!')
        break
    else:
        if m1 > n:
            print('this number is between 1 and %d'%m1)
        else:
            print('this number is between %d and 100'%m1)
    leap +=1
if leap == 6:
    print('Unfortunately, the number is %d'%n)

