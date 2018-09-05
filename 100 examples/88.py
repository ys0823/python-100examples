#-------------------------------------------------------------------------------
#题目：python通过collections解决约瑟夫问题
#要求：据说著名犹太历史学家 Josephus有过以下的故事：
#在罗马人占领乔塔帕特后，39 个犹太人与Josephus及他的朋友躲到一个洞中，
#39个犹太人决定宁愿死也不要被敌人抓到，于是决定了一个自杀方式，41个人排成一个圆圈，
#由第1个人开始报数，每报数到第3人该人就必须自杀，然后再由下一个重新报数，
#直到所有人都自杀身亡为止。然而Josephus 和他的朋友并不想遵从，Josephus要他的朋友先假装遵从，
#他将朋友与自己安排在第16个与第31个位置，于是逃过了这场死亡游戏。
#2018-9-2
#-------------------------------------------------------------------------------
'''
a = [x for x in range(1,42)]
del_number = 3
for i in range(1,42):
    print(del_number)
    del a[del_number]
    del_number = (del_number + 3) % len(a)
'''

import collections
def ysf(a, b):
    d = collections.deque(range(1, a+1))
    print(d)
    while d:
        d.rotate(-b) #环左移b位
        print(d.pop())
if __name__ == '__main__':
    ysf(41, 3)
'''
def solve(n, m):
    list = range(n)
    m -= 1
    k = m%n
    while(len(list) >1):
        del list[k]
        k = (k + m) % len(list)
    return list[0]
print(solve(41,3))
'''


