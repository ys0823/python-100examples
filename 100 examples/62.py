#-----------------------------------------------------------
#题目：往文件中所有添加指定的前缀
#举例：
#比如文中: print是一个函数
#文本文件强制二进制编码
#-----------------------------------------------------------
f_r = open('E:\\叶盛\\研究生学习\\python\\100 例\\62\\test.txt')
f_w = open('E:\\叶盛\\研究生学习\\python\\100 例\\62\\test.txt','w')
i = 0
while True:
    i = i+1
    line = f_r.readline()
    if not line:
        break
    f_w.write('%02d' % (i) + '.Python 3.0:  #' + line)
f_r.close()
f_w.close()


