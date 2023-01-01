# https://www.acmicpc.net/problem/1546

import sys
input()
alist = list(map(int,sys.stdin.readline().split()))
cmax = max(alist)
for i in range(len(alist)):
    alist[i] = alist[i] / cmax*100
print(sum(alist)/len(alist))