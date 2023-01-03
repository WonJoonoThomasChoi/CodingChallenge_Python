# https://www.acmicpc.net/problem/10163

import sys

alist = [[0] * 1001  for x in range(1001)]

n = int(sys.stdin.readline())
for i in range(n):
    x, y, w, h = list(map(int, sys.stdin.readline().split()))
    for j in range(y, y+h):
        for k in range(x, x+w):
            alist[j][k] = i+1
for i in range(1, n+1):
    count = 0
    for j in alist:
        count += j.count(i)
    print(count)