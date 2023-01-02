# https://www.acmicpc.net/problem/2947

import sys
alist=list(map(int,sys.stdin.readline().split()))
ans=sorted(alist)
while True:
    for i in range(4):
        if alist[i]>alist[i+1]:
            alist[i],alist[i+1]=alist[i+1],alist[i]
            print(" ".join(map(str,alist)))
    if alist==ans:
        break