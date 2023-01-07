# https://www.acmicpc.net/problem/9465

import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    alist = list(map(int, sys.stdin.readline().split()))
    blist = list(map(int, sys.stdin.readline().split()))
    if n == 1:
        print(max(alist[0], blist[0]))
        continue
    dp = [0]*n
    alist[1] += blist[0]
    blist[1] += alist[0]
    for i in range(2, n):
        alist[i] += max(blist[i-1], blist[i-2])
        blist[i] += max(alist[i-1], alist[i-2])
    print(max(alist[-1],blist[-1]))