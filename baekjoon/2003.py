# https://www.acmicpc.net/problem/2003

import sys

n, target = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
lp, rp, count = 0, 1, 0
total = nums[0]
while rp < n+1:
    if rp == n and total < target:
        break
    if total == target:
        count += 1
        total -= nums[lp]
        lp += 1

    elif total > target:
        total -= nums[lp]
        lp += 1
    elif total < target:
        total += nums[rp]
        rp += 1
print(count)
