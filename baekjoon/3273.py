# https://www.acmicpc.net/problem/3273

import sys
n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
count, lp, rp = 0, 0, n-1
target = int(sys.stdin.readline())

while lp <rp:
    temp = nums[lp] + nums[rp]
    if temp == target:
        count+=1
        lp+=1
        rp-=1
    elif temp > target:
        rp-=1
    elif temp < target:
        lp+=1
print(count)