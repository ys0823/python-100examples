#-------------------------------------------------------------------
#题目：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
#例如：我下载一个哈利波特全集，看一下效果
#2018-8-28
#-------------------------------------------------------------------
'''
import glob
from collections import Counter
import re
def list_txt():
    return glob.glob('E:\\叶盛\\研究生学习\\python\\100 例\\73\\'
                     'Harry Potter and The Chamber of Secrets.txt')

def wc(filename):
    exclude_words = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 'this'
        ,'s', 'is', 'are', 'a', 'with', 'as', 'an']
    datalist = []
    with open('E:\\叶盛\\研究生学习\\python\\100 例\\73\\Harry Potter and The Chamber of Secrets.txt','r') as f:
        for line in f:
            content = re.sub('\'|,>|\.','',line.lower())
            datalist.extend(content.strip().split(' '))

    wordlst = Counter(datalist)
    for word in exclude_words:
        wordlst[word] = 0
    return wordlst.most_common(1)

def most_comm():
    all_txt = list_txt()
    for txt in all_txt:
        print(wc(txt))

if __name__ =='__main__':
    print(list(map(wc, list_txt())))
'''

import os
import re
def findWord(DirPath):
    if not os.path.isdir(DirPath):
        return
    fileList = os.listdir(DirPath)
    reObj = re.compile('\b?(\w+)\b?') #根据包含的正则表达式的字符串创建模式对象
    for file in fileList: #遍历文件目录
        filePath = os.path.join(DirPath, file)
        if os.path.isfile(filePath) and os.path.splitext(filePath)[1] =='.txt':
            with open(filePath) as f:
                data = f.read()
                words = reObj.findall(data) #返回的总是正则表达式在字符串中所有匹配结果的列表
                wordDict = dict()
                for word in words:
                    word = word.lower() #将字符串转换成小写
                    if word in ['a', 'the' ,'to']: #如果word是a,the,to
                        continue
                    if word in wordDict:
                        wordDict[word] +=1
                    else:
                        wordDict[word] = 1
            ansList = sorted(wordDict.items(), key = lambda t:t[1] ,reverse=True)
            print('file: %s->the most word:%s' % (file, ansList[1]))

if __name__ =='__main__':
    findWord('E:\\叶盛\\研究生学习\\python\\100 例\\73')