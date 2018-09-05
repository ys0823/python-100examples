import requests

status = requests.get("http://www.baidu.com").status_code #尝试获取某个网页
print(status)

import urllib.request
codel = urllib.request.urlopen("https://www.baidu.com").code #code抓取异常

print(codel)