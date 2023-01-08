# https://www.acmicpc.net/problem/2559

import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
lp, rp = 0, k
ans = cmax = sum(nums[:k])
while rp < n:
    ans = ans - nums[lp] + nums[rp]
    cmax = max(ans, cmax)
    lp += 1
    rp += 1
print(cmax)
