# https://www.acmicpc.net/problem/2230

import sys

n, m = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()
if n==1:
    print(0)
    sys.exit()

cmin = float('inf')
lp=0
rp=1
while lp<n and rp<n:
    diff = nums[rp]-nums[lp]
    if diff < m:
        rp+=1
    else:
        lp+=1
        cmin = min(cmin, diff)
print(cmin)