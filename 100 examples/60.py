#-------------------------------------------------------
#题目：对html页面获取内容。我把下面的页面源码复制出来，然后处理
#举例：http://www.cangqionglongqi.com/hunyeshiyichongshenghuo/1834839.html
#2018-8-21
#--------------------------------------------------------

import urllib.request
def read_pageHtml(url):
    file = urllib.request.urlopen(url)
    data = file.read()
    return data
url = "http://www.cangqionglongqi.com/hunyeshiyichongshenghuo/1834839.html"
data = read_pageHtml(url)
print(data)

def storageToLocalFiles(storagePath, data):
    fhandle = open(storagePath, 'wb')
    fhandle.write(data)
    fhandle.close()
storagePath = 'C:\\Users\\admin\\Desktop\\1.html'
#data = read_pageHtml(url)
storageToLocalFiles(storagePath, data)

'''
import urllib.request
from bs4 import BeautifulSoup
with open('http://www.cangqionglongqi.com/hunyeshiyichongshenghuo/1834839.html','r') as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc,'html.parser')

import re
docks = soup.prettify(formatter = 'html')
mkds = BeautifulSoup(docks, 'html.parser')
for x in mkds.find_all(id = 'content'):
    string = x.get_text
    string.replace(u'\xa0',u'')
    with open('h.txt','a+',encoding='utf-8') as f:
        f.write(string)
'''
'''
import re
from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.cangqionglongqi.com/hunyeshiyichongshenghuo/1834839.html'
# connect to a URL
web = urllib.request.urlopen(url)
# read html code
html = web.read()
# print html
soup = BeautifulSoup(html,'html.parser')
prety = soup.prettify()
# print prety
pointed_div = soup.findAll(name="div", attrs={"class":re.compile("forFlow")})# 筛选标签为div且属性class为forFlow的源码
print(pointed_div)
'''