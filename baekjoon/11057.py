# https://www.acmicpc.net/problem/11057

import sys
alist = [1] * 10
n = int(sys.stdin.readline())
for _ in range(n-1):
    temp = [0] * 10
    temp[0]=alist[0]
    for i in range(1,10):
        temp[i] = temp[i-1] + alist[i]
    alist = temp.copy()
print(sum(alist)%10007)

