#---------------------------------------------------
#题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，
#加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，
# 再将第一位和第四位交换，第二位和第三位交换。
#2018-8-20
#---------------------------------------------------
n = int(input('please input a number:\n'))
a = n/1000
b = n%1000/100
c = n%1000%100/10
d = n%1000%100%10
a = (a + 5)%10
b = (b + 5)%10
c = (c + 5)%10
d = (d + 5)%10
print('the final number is %d%d%d%d'%(d,c,b,a))
