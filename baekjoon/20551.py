# https://www.acmicpc.net/problem/20551

import sys


def binary_search(target):
    start, end = 0, n - 1
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            if end == start:
                return mid
            else:
                ans = mid
                end = mid - 1
        elif nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
    return ans


n, m = map(int, sys.stdin.readline().split())
nums = sorted([int(sys.stdin.readline()) for _ in range(n)])
for _ in range(m):
    print(binary_search(int(sys.stdin.readline())))
