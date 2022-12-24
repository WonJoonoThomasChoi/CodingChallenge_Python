#https://www.acmicpc.net/problem/11722

import sys
t = int(sys.stdin.readline())
for i in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    alist=[ x for x in range(n+1) ]
    for j in range(k):
        for i in range(1,n+1):
            alist[i]=alist[i-1]+alist[i]
    print(alist[-1])