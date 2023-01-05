# https://www.acmicpc.net/problem/14916

import sys
count =0
n = int(sys.stdin.readline())

alist = [-1] * (n+1)

alist[2]=1
alist[4]=2
alist[5]=1
alist[6]=3
alist[7]=2
alist[8]=4

for i in range(9,n+1):
    alist[i] = min(alist[i-2], alist[i-5]) + 1
print(alist[n])
