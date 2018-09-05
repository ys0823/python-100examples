#---------------------------------------------
#七夕专用:打印一个心形
#2018-8-15
#--------------------------------------------
'''
# -*- codding=utf-8 -*-
import time
str_n = input('please input the word you want say in Tanabata Festival:\n')
n = [m for m in str_n.split()]
char = n
allchar =[]
for y in range(12,-12,-1):
    lst = []
    lst_con =''
    for x in range(-30,30):
        f = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
        if f <=0:
            lst_con +=char[(x)%len(char)]
        else:
            lst_con +=''
    lst.append(lst_con)
    allchar +=lst
print('\n'.join(allchar))
    #time.sleep(1)
'''
class bcolors:
    PINK ='\033[95m'
    LIGHTBLUE = '\033[94m'
    LIGHTGREEN = '\033[92m'
    WARNING = '\033[93m'
    LIGHTRED = '\022[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m' #黑体字
    UNDERLINE = '\033[4m' #下划线

str_n = input('please input the word you want to say in Tanabata Festival:\n')
n = [m for m in str_n.split()]
sentence = n
#sentence = "learn"
for char in sentence:
   allChar = []
   for y in range(12, -12, -1):
       lst = []
       lst_con = ''
       for x in range(-35, 35):
            formula = ((x*0.04)**2+(y*0.1)**2-1)**3-(x*0.04)**2*(y*0.1)**3
            if formula <= 0:
                lst_con += char[(x) % len(char)]
            else:
                lst_con += ' '
       lst.append(lst_con)
       allChar += lst
   #print('\n'.join(allChar))
   print(bcolors.PINK + '\n'.join(allChar) + bcolors.ENDC)


