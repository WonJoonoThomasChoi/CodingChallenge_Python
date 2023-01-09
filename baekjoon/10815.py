# https://www.acmicpc.net/problem/10815

import sys

n, base_num = int(sys.stdin.readline()) , sorted(list(map(int, sys.stdin.readline().split())))
m, check_num = int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split()))
ans_list = [0] * m

def binary_search(idx, start, end):
    if start > end:
        return
    check = check_num[idx]
    mid = (start + end) // 2
    if base_num[mid] == check:
        ans_list[idx] = 1
        return
    elif base_num[mid] > check:
        binary_search(idx, start, mid - 1)
    else:
        binary_search(idx, mid + 1, end)

for i in range(len(check_num)):
    binary_search(i, 0, n - 1)
print(*ans_list)