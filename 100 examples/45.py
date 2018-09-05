#-------------------------------------------
#假如一个数组中的元素，其前面的部分等于后面的部分，那么这个点的位序就是平衡点
#求一个列表是否存在平衡点
#2018-8-14
#-------------------------------------------
def balance_point(thy_list):
    num = len(thy_list)
    if num > 3:
        for i in range(num):
            if i ==0:
                pass
            else:
                list1 = thy_list[:i]
                list2 = thy_list[i+1:]
                sum1 = sum(list1)
                sum2 = sum(list2)
                if sum1 == sum2:
                    return ('平衡点:%d,值为:%d'%(i,thy_list[i]))
        return ('无平衡点')
    else:
        return('至少输入3个元素以上的列表')
if __name__ =='__main__':
    str_n = input("please input a list:\n")
    n = [int(m) for m in str_n.split()]
    print(balance_point(list(n)))