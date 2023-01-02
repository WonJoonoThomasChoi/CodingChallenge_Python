# https://www.acmicpc.net/problem/1551

import sys
n, repeat = list(map(int, sys.stdin.readline().split()))
alist = list(map(int, sys.stdin.readline().split(',')))
for _ in range(repeat):
    for i in range(n-1):
        alist[i] = (alist[i+1] - alist[i])

print(','.join(map(str, alist[:n-repeat])))