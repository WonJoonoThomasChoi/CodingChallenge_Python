# https://www.acmicpc.net/problem/2563
import sys
alist = [[0 for i in range(100)]for i in range(100)]
for _ in range(int((sys.stdin.readline()))):
    x, y = list(map(int, sys.stdin.readline().split()))
    for i in range(x-1,x+9):
        for j in range(y-1,y+9):
            alist[i][j] = 1
print (sum( [sum(x) for x in alist] ))


