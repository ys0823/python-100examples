#-----------------------------------------------------
#题目：一个商城在搞抽奖的活动，需要在搞活动的宣传单上印刷优惠卷的验证码，
# 验证码规定20位,生成100个
#2018-8-24
#-----------------------------------------------------
import random
import string
forSelect = string.ascii_letters + string.digits #string用法
def generate_code(count, length):
    ra = ''
    for x in range(count):
        Re = ''
        for y in range(length):
            Re = random.choice(forSelect) #随机选取一个字符
            #print('Re is:%s'%Re)
        ra += Re
        #print('rais:%s'%ra)
    return ra
if __name__ =='__main__':
    for i in range(100):
        count = generate_code(20,20)
        print(count)
'''
import random
import string
forSelect = string.ascii_letters + string.digits
def generate_code(length):
    ra = ''
    for y in range(length):
        #re = ''
        Re = random.choice(forSelect) #随机选取一个字符
            #print('Re is:%s'%Re)
        #print('rais:%s'%ra)
        ra += Re
    return ra
if __name__ =='__main__':
    for i in range(100):
        count = generate_code(20)
        print(count)
'''
