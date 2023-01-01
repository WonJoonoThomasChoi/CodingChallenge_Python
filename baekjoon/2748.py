# https://www.acmicpc.net/problem/2748

import sys
n = int(sys.stdin.readline())

alist = [0,1]
for i in range(n-1):
    alist.append(alist[i+0] + alist[i+1])
print(alist[-1])