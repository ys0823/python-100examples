#-------------------------------------------------------------
#题目：使用python写一个ip接口查询，并返回属于地域和国籍。
#要求：使用python3写，可以尝试使用urllib.request方法。
#2018-9-5
#-------------------------------------------------------------
import sys, os, requests, json
import urllib.request
def get_ip_area(ip):
    try:
        apiurl = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s'%ip
        content = urllib.request.urlopen(apiurl).read().decode('utf-8')
        print(content)
        data = json.loads(content)['data']
        code = json.loads(content)['code']
        if code == 0:
            print(data['country_id'])
            print(data['country'])
            print(data['area'])
            print(data['city'])
            print(data['reigon'])
            print(data['isp'])
        else:
            print(data)
    except Exception as ex:
        print(ex)
if __name__ == '__main__':
    ip = '14.131.11.203'
    get_ip_area(ip)