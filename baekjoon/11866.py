# https://www.acmicpc.net/problem/11866

import sys

n, k = map(int, sys.stdin.readline().split())
alist = list(range(1, n+1))
blist = []
i = 0
while alist:
    i = (i+k-1) % len(alist)
    blist.append(alist.pop(i))
print("<" +", ".join(map(str, blist)) + ">")