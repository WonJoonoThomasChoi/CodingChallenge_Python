# https://www.acmicpc.net/problem/10844

import sys
alist = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
temp = [0] * 10
for _ in range(int(sys.stdin.readline())-1):
    for i in range(10):
        if i == 0:
            temp[i] = alist[i + 1]
        elif i == 9:
            temp[i] = alist[i - 1]
        else:
            temp[i] = alist[i - 1] + alist[i + 1]
    alist = temp.copy()
print(sum(alist)% 1000000000)
