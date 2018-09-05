#-------------------------------------------------------
#题目：使用python开发一个简单的socket程序，在两台电脑之间传输消息。
#要求：分为客户端和服务端，在客户端上发给服务端，服务端打印出来。
#2018-9-2
#-------------------------------------------------------
#服务端
import os
from socket import *
host = '127.0.0.3'
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print('Waiting to receive message...')
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    data = data.decode()
    print('Received message: ' + data)
    if data == 'exit':
        break
UDPSock.close()
os._exit(0)
