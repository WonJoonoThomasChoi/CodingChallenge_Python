# https://www.acmicpc.net/problem/2417

import sys
n = int(sys.stdin.readline())
if n == 0:
    print(0)
    sys.exit()
start, end = 1, n
while start <= end:
    mid = (start + end) // 2
    if mid ** 2 >= n:
        end = mid - 1
    else:
        start = mid + 1
print(start)
