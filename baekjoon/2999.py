# https://www.acmicpc.net/problem/2999

import sys
n = sys.stdin.readline().rstrip()
l = len(n)
for r in range(l+1):
    for c in range(r,l+1):
        if r*c == l:
            R=r
            C=c

alist = [["" for x in range(C)] for y in range(R)]
count=0
for i in range(C):
    for j in range(R):
        alist[j][i] = n[count]
        count+=1

for i in range(R):
    for j in range(C):
        print(alist[i][j],end="")