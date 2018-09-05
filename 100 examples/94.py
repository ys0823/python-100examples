#----------------------------------------------------
#题目：要求对目录下的文件进行增和删除的监控，如果有增和删打印出来，并打印文件名。
#要求：使用python3使用最简单的方法。
#2018-9-4
#----------------------------------------------------
import os,time
path_to_watch = '.'
before = dict([(f,None) for f in os.listdir(path_to_watch)])
while 1:
    time.sleep(10)
    after = dict([(f, None) for  f in os.listdir(path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added:
        print('Added: ' ,','.join(added))
    if removed:
        print('Removed: ',','.join(removed))
    before = after


