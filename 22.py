#-------------------------------------------
#简述：已知有两支乒乓球队要进行比赛，每队各出三人；
#甲队为a,b,c三人，乙队为x,y,z三人；
#抽签决定比赛名单。
#问题：有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
#2018-8-5
#-------------------------------------------

for i in range(ord('x'), ord('z')+1):
    for j in range(ord('x') ,ord('z')+1):
        if i!=j:
            for k in range(ord('x'),ord('z')+1):
                if(i!=k) and (j!=k):
                    if (i!=ord('x')) and (k!=ord('x')) and (k!=ord('z')):
                        print('other is a--%s\tb--%s\tc--%s'%(chr(i),chr(j),chr(k)))
