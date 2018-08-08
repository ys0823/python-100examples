'''
import string
s = input('请输入一串字符:\n')
l = 0
a = 0
b = 0
c = 0
for i in s:
    if c.isalpha():#如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
        l = l+1
    elif c.isspace():#检测字符串是否只由空格组成
        a = a+1
    elif c.isdigit(): #检测字符串是否只由数字组成
        b = b+1
    else:
        c += 1
print('char =%d,space=%d,digit=%d,others=%d'%(l,a,b,c))
'''
lst = list(input('请输入一行字符，可以是任意字符：'))

iLetter = []
iSpace = []
iNumber = []
iOther = []

for i in range(len(lst)):
    # ord() 函数用于求字符串的ASCII码
    if ord(lst[i]) in range(65, 91) or ord(lst[i]) in range(97, 123):
        iLetter.append(lst[i])
    elif lst[i] == ' ':
        iSpace.append(' ')
    elif ord(lst[i]) in range(48, 58):
        iNumber.append(lst[i])
    else:
        iOther.append(lst[i])

print('中英文字母个数：%s' % len(iLetter))
print('空格个数：%s' % len(iSpace))
print('数字个数：%s' % len(iNumber))
print('其它字符个数：%s' % len(iOther))