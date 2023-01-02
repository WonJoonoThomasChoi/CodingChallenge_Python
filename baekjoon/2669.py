# https://www.acmicpc.net/problem/2669

import sys
alist = [[0]*100 for _ in range(100)]
for i in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            alist[i][j] = 1
cnt = 0
for i in alist:
    cnt += i.count(1)
print(cnt)
