# https://www.acmicpc.net/problem/2805

import sys

n, target = map(int, sys.stdin.readline().rstrip().split())
alist = list(map(int, sys.stdin.readline().split()))
lp, rp = 1, max(alist)

while lp<=rp:
    cmin = (lp + rp) // 2
    cut = sum([x-cmin for x in alist if x>cmin])

    if cut >= target:
        lp = cmin+ 1
    else:
        rp = cmin- 1
print(rp)



