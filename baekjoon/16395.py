# https://www.acmicpc.net/problem/16395

import sys
n, k = map(int, sys.stdin.readline().split())
dp=[0]*(n+1)
dp[1]=1



for i in range(2,n+1):
    for j in range(1,i):
        dp[i]+=dp[j]

print(dp[n])


