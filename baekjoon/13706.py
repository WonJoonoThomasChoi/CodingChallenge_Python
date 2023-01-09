# https://www.acmicpc.net/problem/13706

import sys
n = int(sys.stdin.readline())
start = 0
end = n
while start<=end:
    mid = (start+end) // 2
    if mid**2 == n:
        print(mid)
        break
    elif mid**2 > n:
        end = mid - 1
    else:
        start = mid + 1
