#--------------------------------------
#python基础函数调用方法练习
#2018-8-10
#---------------------------------------

def hello_python():
    print("python3v")

def three_hellos():
    for i in range(10):
        hello_python()

if __name__ == "__main__":
    three_hellos()