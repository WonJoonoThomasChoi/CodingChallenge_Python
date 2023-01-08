# https://www.acmicpc.net/problem/2470

import sys
n = int(sys.stdin.readline())
alist = list(map(int, sys.stdin.readline().split()))
alist.sort()
lp, rp, diff, ans =0, n-1,float('inf'), [0,0]
while lp < rp:
    if abs(alist[lp]+alist[rp]) < diff:
        diff = abs(alist[lp]+alist[rp])
        ans = [alist[lp], alist[rp]]
    if alist[lp] + alist[rp] > 0:
        rp -= 1
    else:
        lp += 1
print(*ans)