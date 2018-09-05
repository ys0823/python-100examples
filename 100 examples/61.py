#---------------------------------------------------------------------
#题目：假如要读取的test.txt文件内容如下:
#举例：test.txt文件中有如下内容：
#Python
#Perl
#Java
#Shell
#2018-8-22
#---------------------------------------------------------------------
with open('E:\\叶盛\\研究生学习\\python\\100 例\\61\\test.txt','r') as f:
    f1 = f.read()
print(f1)
'''
list = []
f = open('E:\\叶盛\\研究生学习\\python\\100 例\\61\\test.txt','r')
#with open('E:\\叶盛\\研究生学习\\python\\100 例\\61\\test.txt','r') as f:
while True:
    f1 = f.readline()
    list.append(f1.strip())
    if len(f1) ==0:
        break
for i in range(0,len(list)):
    print(list[i])
f.close()
'''

