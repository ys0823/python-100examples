#------------------------------------------------------
#题目：使用Python读取file.txt，当用户输入敏感词语，则用 星号 * 替换，
#例如：当用户输入「北京是个好城市」，则变成「**是个好城市」。
#2018-8-27
#------------------------------------------------------
w = input('请输入一句话:\n').strip()
with open('E:\\叶盛\\研究生学习\\python\\100 例\\72\\file.txt','r') as f:
    for line in f:
        new_line = line.strip()
        if new_line in w:
            w = w.replace(new_line,'*'*len(new_line))
print(w)
'''
world_filter = set()
with open('E:\\叶盛\\研究生学习\\python\\100 例\\72\\file.txt','r') as f:
    for w in f.readlines():
        world_filter.add(w.strip())
while True:
    s = input('please enter your key words:')
    if s == 'exit':
        break
    for w in world_filter:
        if w in s:
            s = s.replace(w,'*'*len(w))
    print(s)
'''




