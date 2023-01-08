# https://www.acmicpc.net/problem/1253

import sys

n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))

count = 0
for i in range(n):
    temp = nums[0:i] + nums[i+1:]
    target = nums[i]
    lp, rp = 0, len(temp) - 1
    while lp<rp:
        if temp[lp] + temp[rp] == target:
            count+=1
            break
        elif temp[lp] + temp[rp] > target:
            rp-=1
        elif temp[lp] + temp[rp] < target:
            lp+=1
print(count)
'''
[2, 3, 3, 4, 5, 5, 6, 6, 8, 9, 12, 15, 16]
[0 ,0, 0, 0, 1, 1, 1, 1, 1, 1, 1,  1,  1 ]

'''
