#------------------------------------------------------
#题目：写一个摇骰子游戏，要求用户压大小，赔率一赔一。
#要求：三个骰子，摇大小，每次打印摇骰子数。
#2018-8-30
#------------------------------------------------------
import random
print('恭喜你来到澳门豪华赌场')
money = int(input('请押赌注筹码:\n'))
s = input('请押大押小:\n')

def Result_size():
    n = []
    leap = ''
    for i in range(0,3):
        n.append(random.randint(1,7))
    m = sum(n)
    if m <= 10 and m>=3:
        leap = 'small'
    if m <= 18 and m>=11:
        leap = 'big'
    return leap,m,n

size , result, n= Result_size()
if s == size:
    print('骰子点数为%d,%d,%d'%(n[0],n[1],n[2]))
    print('恭喜你,押对了!,你可以获得%d块钱'%(money*2))
if s != size:
    print('骰子点数为%d,%d,%d'%(n[0], n[1], n[2]))
    print('很遗憾,你押错了,你的赌注将全部归赌场所得')
print('游戏结束')


