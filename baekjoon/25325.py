# https://www.acmicpc.net/problem/25325

import sys
n, alist = int(sys.stdin.readline()), list(sys.stdin.readline().split())
adict = {}
for i in alist:
    adict[i] = 0

for i in range(n):
    for j in list(sys.stdin.readline().split()):
        adict[j] += 1
alist = sorted(adict, key=lambda x: adict[x], reverse=True)
for i in alist:
    print(i, adict[i])