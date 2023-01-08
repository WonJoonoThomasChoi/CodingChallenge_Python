# https://www.acmicpc.net/problem/7453

import sys

n = int(sys.stdin.readline())
alist, blist, clist, dlist = [], [], [], []

for i in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    alist.append(a)
    blist.append(b)
    clist.append(c)
    dlist.append(d)

adict = {}
for i in range(n):
    for j in range(n):
        adict[alist[i] + blist[j]] = adict.get(alist[i] + blist[j], 0) + 1

ans = 0
for c in clist:
    for d in dlist:
        ans += adict.get((-c-d),0)
print(ans)
