#-----------------------------------------
#五家共井，甲二绠（汲水用的井绳）不足，如（接上）乙一绠；乙三绠不足，如丙一绠；
# 丙四绠不足，如丁一绠；丁五绠不足，如戊一绠；戊六绠不足，如甲一绠，皆及
#https://blog.csdn.net/songjs19931206/article/details/42421053
#2018-8-13
#-----------------------------------------
for k in range(1,5):
    for e in range(1,100):
        a = 721 * k -6 * e
        b = 721 * k -2 * a
        c = 721 * k -3 * b
        d = 721 * k -4 * c
        e = 721 * k -5 * d

        h1 = a + 6 * e
        h2 = b + 2 * a
        h3 = c + 3 * b
        h4 = d + 4 * c
        h5 = e + 5 * d

        if h1 ==h2 ==h3 ==h4 ==h5:
            print('井深:%d\n 甲家绳长%d,乙家绳长%d,丙家绳长%d,丁家绳长%d,戊家绳长%d'%(h1,a,b,c,d,e))
