# https://www.acmicpc.net/problem/7568

import sys
alist=[]
for _ in range(int(sys.stdin.readline())):
    alist.append(list(map(int,sys.stdin.readline().split())))

for i in alist:
    rank=1
    for j in alist:
        if i[0] < j[0] and i[1] < j[1] :
            rank+=1
    print(rank, end=' ')
