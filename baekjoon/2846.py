# https://www.acmicpc.net/problem/2846

import sys
input()
alist = list(map(int, sys.stdin.readline().split()))
ans = 0
cmin=alist[0]
cmax=0
prev=alist[0]
for i in range(1, len(alist)):
    if alist[i]>prev:
        cmax = max(cmax, alist[i])
        ans = max(ans, cmax-cmin)
    else:
        cmin = alist[i]
        cmax = 0
    prev=alist[i]
print(ans)