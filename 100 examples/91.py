#----------------------------------------------------------
#题目：使用python3从N个数组中，进行排列组合，打印排列后的所有列表。
#要求：尝试使用笛卡尔算法
#2018-9-3
#----------------------------------------------------------
class Cartesian():
    def __init__(self, datagroup):
        self.datagroup = datagroup
        self.counterIndex = len(datagroup) - 1
        self.counter = [ 0 for i in range(0, len(self.datagroup))]

    def countlength(self):
        i = 0
        length = 1
        while(i < len(self.datagroup)):
            length *= len(self.datagroup[i])
            i += 1
        return length

    def handle(self):
        self.counter[self.counterIndex] += 1
        if self.counter[self.counterIndex] >= len(self.datagroup[self.counterIndex]):
            self.counter[self.counterIndex] = 0
            self.counterIndex -= 1
            if self.counterIndex >= 0:
                self.handle()
            self.counterIndex = len(self.datagroup) - 1

    def assemble(self):
        length = self.countlength()
        i = 0
        while(i < length):
            attrlist = []
            j = 0
            while(j <len(self.datagroup)):
                attrlist.append(self.datagroup[j][self.counter[j]])
                j = j+1
            print(attrlist)
            self.handle()
            i += 1

if __name__ == '__main__':
    datagroup = [['aa1', ], ['bb1', ], ['cc1', 'cc2' ,'cc3']]
    cartesian = Cartesian(datagroup)
    cartesian.assemble()


