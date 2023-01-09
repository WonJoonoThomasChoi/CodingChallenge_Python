# https://www.acmicpc.net/problem/2512

import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())
ans = [0] * n
if sum(nums) <= target:
    print(max(nums))
    sys.exit()
else:
    start, end = 0, max(nums)
    while start <= end:
        mid = (start + end) // 2
        if sum([i if i < mid else mid for i in nums]) <= target:
            start = mid + 1
        else:
            end = mid - 1
    print(end)