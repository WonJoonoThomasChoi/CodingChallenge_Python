# https://www.acmicpc.net/problem/1806

import sys
n, target = map(int, sys.stdin.readline().split())
alist = list(map(int, sys.stdin.readline().split()))
lp = 0
rp = 0
total = alist[0]
min_length = float('inf')

while True:
    if total >= target:
        total -= alist[lp]
        min_length = min(min_length, rp - lp + 1)
        lp+=1
    elif total < target:
        rp += 1
        if rp == n:
            break
        total += alist[rp]
print(min_length if min_length != float('inf') else 0)
