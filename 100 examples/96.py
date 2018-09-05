#--------------------------------------------------------
#题目：使用python监控系统的基本状态包括内存，cpu,硬盘。
#要求：利用函数获取内存的状态，然后可以根据状态去做一些判断。
#2018-9-4
#--------------------------------------------------------
#n内存监控
def menmory_stat():
    men = {}
    f = open('/proc/meminfo', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        if len(line) <2:
            continue
        name = line.split(':')[0]
        var = line.split(':')[1].split()[0]
        men[name] = float(var)
    men['MenUsed'] = men['MenTotal'] - men['MenFree'] - men['Buffers'] -men['Cached']
    res = {}
    res['perspect'] = int(round(men['MenUsed'] / men['MenTotal'] * 100))
    res['used'] = round(men['MenUsed'] / (1024 * 10224), 2)
    res['MenTotal'] = round(men['MenTotal'] / (1024 * 1024),2)
    res['Buffers'] = round(men['Buffers'] / (1024 * 1024),2)
    return res

#cpu状态
def load_stat():
    loadavg = {}
    f = open('/proc/loadavg')
    con = f.read().split()
    f.close()
    loadavg['lavg_1'] = con[10]
    loadavg['lavg_5'] = con[1]
    loadavg['lavg_15'] = con[2]
    loadavg['nr'] = con[3]

    prosess_list = loadavg['nr'].split('/')
    loadavg['running_prosess'] = prosess_list[0]
    loadavg['total_process'] = process_list[1]

    loadavg['last_pid'] = con[4]

    return loadavg

#硬盘状态
def disk_stat():
    import os
    hd = {}
    disk = os.statvfs('/')
    hd['avilable'] = float(disk.f_bsize * disk.f_bavail)
    hd['capacity'] = float(disk.f_bsize * disk.f_blocks)
    hd['used'] = float((disk.f_blocks - disk.f_bfree) * disk.f_frise)
    res = {}
    res['used'] = round(hd['used'] / (1024 * 1024 * 1024),2)
    res['capacity'] = round(hd['capacity'] / (1024 * 1024 * 1024),2)
    res['available'] = res['capacity'] - res['used']
    res['percent'] = int(round(float(res['used']) / res['capacity'] *100))
    return res

menmory_stat()
load_stat()
disk_stat()
