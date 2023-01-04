# https://www.acmicpc.net/problem/2999

import sys
txt = sys.stdin.readline().rstrip()
n = len(txt)
maxR = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        if i*j == n:
            if i >= j:
                maxR = max(maxR,j)
maxC = n//maxR
print(maxR,maxC)
alist = [["" for x in range(maxR)] for y in range(maxC)]
print(alist)
count=0
for i in range(maxC):
    for j in range(maxR):
        alist[i][j] = txt[count]
        count+=1
print(alist)

for i in range(maxR):
    for j in range(maxC):
        print(alist[j][i],end="")