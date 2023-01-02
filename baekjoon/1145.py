# https://www.acmicpc.net/problem/1145

import sys
alist = list(map(int,sys.stdin.readline().split()))
cmin = min(alist)
while True:
    count=0
    for i in alist:
        if cmin%i==0:
            count+=1
    if count>=3:
        print(cmin)
        break
    else:
        cmin+=1