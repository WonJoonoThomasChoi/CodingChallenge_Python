# https://www.acmicpc.net/problem/1932

import sys

n = int(sys.stdin.readline())
alist = [int(sys.stdin.readline())]
for j in range(1,n):
    temp = list(map(int, sys.stdin.readline().split()))
    for i in range(len(temp)):
        if i == 0:
            temp[i] += alist[i]
        elif i == j:
            temp[i] += alist[i - 1]
        else:
            temp[i] += max(alist[i - 1], alist[i])
    alist= temp.copy()
print(max(alist))



'''
import sys

n = int(sys.stdin.readline())
alist = []
for _ in range(n):
    alist.append(list(map(int, sys.stdin.readline().split())))
for j in range(1,n):
    for i in range(j + 1):
        if i == 0:
            alist[j][i] += alist[j - 1][i]
        elif i == j:
            alist[j][i] += alist[j - 1][i - 1]
        else:
            alist[j][i] += max(alist[j - 1][i - 1], alist[j - 1][i])
    print(alist[j])
print(max(alist[-1]))

'''