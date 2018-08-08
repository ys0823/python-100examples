# Writer: Leo
# @Time: 2018/8/1 19:15
"""哲学家吃饭"""
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, chop1, chop2):
        super().__init__()
        self.name = name
        self.chop1 = chop1
        self.chop2 = chop2

    def run(self):
        name = self.name
        s1 = threading.Lock()
        s2 = threading.Lock()
        while True:
            list1 = []
            if s1.acquire(blocking=True, timeout=1):
                time.sleep(1)
                list1.append(self.chop1)
                if s2.acquire(blocking=True, timeout=1):
                    list1.append(self.chop2)
                    print('philosopher%s eating........' % name)
                    s2.release()
                s1.release()
            if len(list1) == 2:
                break


"""
list2 = []
for i in range(5):
    list2.append(threading.Lock())


def lock(n):
    return list2[n]
"""


def main():
    chopsticks = ['chop1', 'chop2', 'chop3', 'chop4', 'chop5']
    for i in range(5):
        t = MyThread(chr(i + 65), chopsticks[i], chopsticks[(i + 1) % 5])
        t.start()


if __name__ == '__main__':
    main()
