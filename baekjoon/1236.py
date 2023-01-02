# https://www.acmicpc.net/problem/1236

import sys
n, m=map(int, sys.stdin.readline().split())
castle=[]
for i in range(n):
    castle.append(sys.stdin.readline())
row=[0]*n
col=[0]*m
for i in range(n):
    for j in range(m):
        if castle[i][j]=="X":
            row[i]=1
            col[j]=1
print(max(n-sum(row),m-sum(col)))
