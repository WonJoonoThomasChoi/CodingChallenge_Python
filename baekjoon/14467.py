# https://www.acmicpc.net/problem/14467

import sys
n = int(sys.stdin.readline())
adict = {}
alist = [-1] * 10
for i in range(n):
    n, m = map(int, sys.stdin.readline().split())
    if alist[n-1] == -1:
        alist[n-1] = m
    elif alist[n-1] != m:
        alist[n-1] = m
        adict[n] = 1 + adict.get(n, 0)

print( sum(adict.values()) )