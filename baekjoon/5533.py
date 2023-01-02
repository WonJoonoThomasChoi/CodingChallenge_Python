# https://www.acmicpc.net/problem/5533
import copy
import sys
n = int(sys.stdin.readline())
alist = []
for _ in range(n):
    alist.append(list(map(int, sys.stdin.readline().split())))
blist = copy.deepcopy(alist)

for j in range(3):
    for i in range(n):
        for k in range(n):
            if i != k and alist[i][j] == alist[k][j]:
                blist[i][j] = 0
                break
for i in range(n):
    print(sum(blist[i]))
