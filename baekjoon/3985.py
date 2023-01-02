# https://www.acmicpc.net/problem/3985

import sys

alist = [0] * (int(sys.stdin.readline())+1)

cCus = 0
cMax = 0

totalCus = int(sys.stdin.readline())
real = [0] * totalCus
for i in range(totalCus):
    n , m = map(int, sys.stdin.readline().split())
    for j in range(n-1, m):
        if alist[j] == 0:
            alist[j] = i+1
            real[i] += 1
    if cMax < m-n:
        cMax = m-n
        cCus = i+1
print(cCus)
print(real.index(max(real))+1)


