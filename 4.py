#---------------------------------
#简述：要求输入某年某月某日
#提问：求判断输入日期是当年中的第几天？
#Python解题思路分析：
#我们就以3月5日这一天为例。首先把前两个月的加起来，然后再加上5天即本年的第几天。
#这里有一种特殊的情况，就是闰月，遇到这种情况且输入月份大于2时需考虑多加一天。
#---------------------------------
print("please input the date:")
print("the year is: ")
y = int(input())
print("the month is: ")
m = int(input())
print("the day is :")
d = int(input())
day = 0
mm = [1,2,3,4,5,6,7,8,9,10,11,12]
dd = [0,31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(0,m):
    if m>=mm[i]:
        day = day+dd[i]
day = day+d
if ((y%4==0) and (y%100 !=0)) or (y%400 == 0):
    day=day+1
print(day)

#以下为参考代码
#coding=utf-8
#写一个函数，计算给定日期是该年的第几天．
'''
def count(year,month,day):
    count = 0
    #判断该年是平年还是闰年
    if year%400==0 or (year%4==0 and year%100!=0):
        print('%d年是闰年，2月份有29天！'%year)
        li1 = [31,29,31,30,31,30,31,31,30,31,30,31]
        for i in range(month-1):
            count += li1[i]
        return count+day
    else:
        print('%d年是平年，2月份有29天！' % year)
        li2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(month-1):
            count +=li2[i]
        return count+day


if __name__ == "__main__":
    year = int(input('请输入年份：'))
    month = int(input('请输入月份：'))
    day = int(input('请输入日期：'))
    count = count(year,month,day)
    print('%d年%d月%d日是今年的第%d天！'%(year,month,day,count))
'''