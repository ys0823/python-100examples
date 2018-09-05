#-------------------------------------------------------
#题目：使用python开发一个简单的socket程序，在两台电脑之间传输消息。
#要求：分为客户端和服务端，在客户端上发给服务端，服务端打印出来。
#2018-9-2
#-------------------------------------------------------
#客户端
import os
from socket import *
from time import ctime
host = '127.0.0.3'
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input ("Enter message to send type 'exit':")
    UDPSock.sendto(('[%s]%s'%(ctime(),data)).encode(),addr)
    if data == 'exit':
        break
UDPSock.close()
os._exit(0)