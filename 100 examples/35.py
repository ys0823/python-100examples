#---------------------------------------
#设置文本颜色
#用class实现
#2018-8-11
#---------------------------------------
class bcolors:
    PINK ='\033[95m'
    LIGHTBLUE = '\033[94m'
    LIGHTGREEN = '\033[92m'
    WARNING = '\033[93m'
    LIGHTRED = '\022[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m' #黑体字
    UNDERLINE = '\033[4m' #下划线
print(bcolors.WARNING+ "python3v 提示:此时文字颜色为浅黄色" +bcolors.ENDC)