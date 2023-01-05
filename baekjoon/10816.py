# https://www.acmicpc.net/problem/10816

import sys
input()
alist = list(map(int, sys.stdin.readline().split()))
adict = {}
for i in alist:
    adict[i] = adict.get(i, 0) + 1
input()
blist = list(map(int, sys.stdin.readline().split()))
for i in blist:
    print(adict.get(i, 0), end=" ")