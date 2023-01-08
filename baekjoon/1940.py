# https://www.acmicpc.net/problem/1940

import sys

n, m = int(sys.stdin.readline()), int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
count, lp, rp = 0, 0, n - 1
while lp < rp:
    temp = nums[lp] + nums[rp]
    if temp == m:
        count += 1
        lp += 1
        rp -= 1
    elif temp > m:
        rp -= 1
    elif temp < m:
        lp += 1
print(count)
