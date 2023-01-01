# https://www.acmicpc.net/problem/1292

import sys

n, m = list(map(int, sys.stdin.readline().split()))

count = 1
index = 0
ans = 0
while index <= m + 1:
    for j in range(count):
        index += 1
        if n <= index <= m:
            ans += count
    count += 1
print(ans)
