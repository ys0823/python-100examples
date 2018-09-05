#-----------------------------------------------------------
#题目：在ip.txt中每行一个ip地址和端口号，代码可循环监控这些ip地址的指定端口是否正常
#要求:ip.txt文件格式 IP port
#2018-9-5
#-----------------------------------------------------------
import socket,time
while 1:
    file_obj = open('ip.txt')
    for line in file_obj:
        try:
            sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(line.split())
            ip = line.split()[0]
            port = int(line.split()[1])
            print(ip, port)
            sc.settimeout(2)
            sc.connect((ip, port))
            timenow = time.localtime()
            datenow = time.strftime('%Y-%m-%d %H:%M:%S',timenow)
            logstr = '%s:%s 连接成功 -> %s \n'%(ip, port, datenow)
            print(logstr)
            sc.close()
        except:
            file = open('log.txt','a')
            timenow = time.localtime()
            datenow = time.strftime('%Y-%m-%d %H:%M:%S', timenow)
            logstr = '%s:%s 连接失败->%s \n'%(ip,port,datenow)
            print(logstr)
            file.write(logstr)
            file.close()
    print('sleep 10.....')
    time.sleep(10)


