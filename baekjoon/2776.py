# https://www.acmicpc.net/problem/2776

import sys


def binary_search(arr, num):
    lp, rp = 0, len(arr) - 1
    while lp <= rp:
        mid = (lp + rp) // 2
        if arr[mid] == num:
            return 1
        elif arr[mid] < num:
            lp = mid + 1
        else:
            rp = mid - 1
    return 0

cases = int(sys.stdin.readline())
for _ in range(cases):
    n, base_nums = int(sys.stdin.readline()), sorted(list(map(int, sys.stdin.readline().split())))
    m, check_nums = int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split()))
    for i in range(m):
        print(binary_search(base_nums, check_nums[i]))
