#--------------------------------
#打印出菱形
'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''
#center()函数:str.center(width[, fillchar])
#以字符串宽度(width)为中心。使用指定的填充字符(fillchar)填充完成
# 默认填充字符(fillchar)是一个空格。

#reversed()函数:
#返回序列seq的反向访问的迭代子
#参数为列表,元组,字符串
#--------------------------------
s ='*'
for i in range(1,8,2):
    print((s*i).center(7))
for i in reversed(range(1,6,2)):
    print((s*i).center(7))
