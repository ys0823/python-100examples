#------------------------------------------------------------
#题目：下面code.txt文件中内容，将
#01 CN Chinese
#02 IN India
#03 HK HongKang
#04 JP Japan
#05 DE Germany
#06 US United States of America
#要文件的内容，每一行文件，写到一个文件，且文件名前面两个字段，如
#文件名为:01CNChinese.txt
#文中内容:01 CN Chinese
#2018-8-22
#------------------------------------------------------------
postfix = '.txt'

with open('E:\\叶盛\\研究生学习\\python\\100 例\\63\\code.txt') as myfile:
    while True:
        lines = myfile.readlines() #readlines将文件内容读取成一个list
        if not lines:
            break
        for line in lines:
            file_out = str(''.join(line.split()[:])+postfix)
            open(file_out,'w').write(line)

