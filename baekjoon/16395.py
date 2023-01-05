# https://www.acmicpc.net/problem/16395

import sys
n, k = map(int, sys.stdin.readline().split())
dp=[0]*(n+1)
dp[0]=1

for j in range(n):
    temp = [0] * (n+1)
    for i in range(1,j+2):
        temp[i] = dp[i-1] + dp[i]
    dp = temp.copy()
print(dp[k])

