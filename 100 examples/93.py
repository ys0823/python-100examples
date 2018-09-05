#---------------------------------------------------
#题目：使用python把每隔一分钟访问200次的IP，加到黑名单。
#要求：每隔一分钟读区一下日志文件，把统计到的Ip添加到黑名单。
#2018-9-4
#---------------------------------------------------
import time
pin = 0
while True:
    ips = []
    fr = open(r'kms10.log')
    fr.seek(pin)
    for line in fr:
        ip = line.split()[0]
        ips.append(ip)
    new_ips = set(ips)
    for new_ip in new_ips:
        if ips.count(new_ips):
            print('加入黑名单的ip是:%s'%new_ip)
    pin = fr.tell()
    time.sleep(60)
