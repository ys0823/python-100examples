#--------------------------------------------------------
#题目：一个HTML文件，找出里面的链接。
#2018-8-24
#--------------------------------------------------------
'''
from bs4 import BeautifulSoup
import urllib
import urllib.request
import sys
def findAllLink(url):
    #    提取网页中的超链接
    # 获取协议，域名
    proto, rest = urllib.splittype(url)
    domain = urllib.splithost(rest)[0]
    #  读取网页内容
    html = urllib.request.urlopen(url).read()
    # 提取超链接
    a = BeautifulSoup(html).findAll('a')
    # 过滤
    alist = [i.attrs['href'] for i in a if i.attrs['href'][0] != 'j']
    #  将形如#comment-text的锚点补全成https://www.ruanyifeng.com/blog/2015/05/co.html,将形如/feed.html补全为https://www.ruanyifeng.com/feed.html
    alist = map(lambda i: proto + '://' + domain + i if i[0] == '/' else url + i if i[0] == '#' else i, alist)
    return alist
url = 'https://www.ruanyifeng.com/blog/2015/05/co.html'
if __name__ == '__main__':
    for i in findAllLink(url):
        print(i)

'''
from HTMLParser import HTMLParser
import urllib2

class myParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag =0
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag =='a':
            for name, value in attrs:
                if name =='href':
                    self.links.append(value)
if __name__=='__main__':
    parser = myParser
    myurl = 'http://www.baidu.com'
    html = urllib2.urlopen(myurl)
    htmlcode = html.read()
    parser.feed(htmlcode)
    print(parser.links)

