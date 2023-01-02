# https://www.acmicpc.net/problem/1652


import sys
n = int(sys.stdin.readline())
totalX = 0
totalY = 0
alist=[]
blist=[]
for i in range(n):
    alist.append(sys.stdin.readline().rstrip())

for i in range(n):
    temp=""
    for j in range(n):
        temp+=(alist[j][i])
    blist.append(temp)

for i in range(len(alist)):
    for j in range(n,1,-1):
        temp = "." * j
        while temp in alist[i]:
            totalX+=1
            alist[i]=alist[i].replace(temp,"X",1)
        while temp in blist[i]:
            totalY+=1
            blist[i]=blist[i].replace(temp,"X",1)
print(totalX,totalY)




