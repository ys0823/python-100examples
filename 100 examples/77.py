#------------------------------------------------------------------------
#题目：一行代码，使用“love”字符串，拼成心
#2018-8-29
#------------------------------------------------------------------------
print('\n'.join([''.join([('Love'[(x-y)%len('Love')]if((x* 0.05) **2+ (y* 0.1) **2-1) **3- (x*0.05) **2* (y*0.1) **3<=0 else  ' ')for x in range(-30,30)])for y in range(30,-30,-1)]))
