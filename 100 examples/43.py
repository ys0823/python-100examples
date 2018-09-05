#-----------------------------------------
#题目：打印楼梯，同时在楼梯上方打印两个笑脸。
#用i控制行，j来控制列，j根据i的变化来控制输出黑方格的个数
#2018-8-14
#-----------------------------------------
import sys
sys.stdout.write(chr(1))
sys.stdout.write(chr(1))
print('')
print('')
for i in range(1,11):
    for j in range(0,i):
        sys.stdout.write(chr(219))
        sys.stdout.write(chr(219))
    print('')
