#-----------------------------------
#让python程序暂停预定时间后再运行，需要用到time.sleep方法。
#time.sleep(t),t为延迟的时间,需要调用import time包
#-----------------------------------
'''
import time
for i in range(100):
    print("%d"%i)
    time.sleep(2)
'''
import time
myD = {1:'a',2:'b'}
for key ,value in dict.items(myD):
    print(key, value)
    time.sleep(1)
