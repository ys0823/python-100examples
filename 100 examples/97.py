#-----------------------------------------------------
#题目：使用python获取系统的ip地址，并打印出来
#2018-9-5
#-----------------------------------------------------
'''
#Linux系统
import socket
import struct
import fcntl
def gettip(ethname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), OX8915, struct.pack('256', ethname[:15]))[20:24])

if __name__ == '__main__':
    print(gettip('eth0'))
'''
import socket
print('当前主机名为:'+socket.gethostname())
print('当前IP地址为:'+socket.gethostbyname(socket.gethostname()))

