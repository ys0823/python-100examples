#---------------------------------------------------------
#题目：爬美女图片，把下面的贴吧里的图片取出来。
#要求：爬取的图片进行重命名，并写入指定的目录下
#例如：从1自动递增，可以统计多少个图片
#2018-8-26
#---------------------------------------------------------
import os
import requests
from bs4 import  BeautifulSoup
url = 'http://tieba.baidu.com/p/2166231880'
html = requests.get(url)
path = 'E:\\叶盛\\研究生学习\\python\\100 例\\70'
#使用自带的html.parser解析
soup = BeautifulSoup(html.text, 'html.parser')
img_urls = soup.findAll('img', bdwater ='杉本有美吧,1280,860')
count = 1
for img_url in img_urls:
    img_src = img_url['src']
    os.path.split((img_src)[1])#如果给出的是一个目录和文件名，则输出路径和文件名
    with open('path' + ('%s.jpg' %count),'wb') as f:
        f.write(('%s.jpg' %count).encode())
    count +=1
