#-------------------------------------------------------------
#取一个任意小于 1 美元的金额，然后计算可以换成最少多少枚硬币。
#硬币有 1美分，5 美分，10 美分，25 美分四种。1 美元等于 100 美分。
#举例来说，0.76 美元换算结果应该是 3 枚 25 美分，1 枚 1 美分。
#类似 76 枚 1 美分，2 枚 25 美分+2 枚 10 美分+1 枚 5 美分+1枚 1 美分这样的结果都是不符合要求的。
#2018-8-19
#-------------------------------------------------------------
'''
n = int(input("please input the money you want change:\n"))
a,b,c,d = 0,0,0,0
a = int(n/25)
n = n- 25*a
if n > 0:
    b = int(n/10)
    n = n - b*10
    if n > 0:
        c = int(n/5)
        n = n - c*5
        if n >0:
            d = n
print("The least coin for %d is 25:%d,10:%d,5:%d,1:%d"%(n,a,b,c,d))
'''
def leastCoin(coinNum):
    coin = [25,10,5,1]
    coinN = []
    for item in coin:
        coinN.append(coinNum/item)
        coinNum = coinNum%item
    return coinN
if __name__ =='__main__':
    coin = int(input('please input the money you want change:\n'))
    coinN = leastCoin(coin)
    print('The least coin for %d is 25:%d,10:%d,5:%d,1:%d'%(coin,coinN[0],coinN[1],coinN[2],coinN[3]))

