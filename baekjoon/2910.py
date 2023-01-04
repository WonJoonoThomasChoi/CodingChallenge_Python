# https://www.acmicpc.net/problem/2910

import sys
n, c = map(int, sys.stdin.readline().split())
alist = list(map(int, sys.stdin.readline().split()))
adict = {}
for i in alist:
    adict[i] = 1 if i not in adict else adict[i] + 1

alist = sorted(adict, key=lambda x: adict[x], reverse=True)
for i in alist:
    print((str(i)+" ")*adict[i], end="")
