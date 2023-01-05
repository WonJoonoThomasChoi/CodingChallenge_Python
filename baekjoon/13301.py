# https://www.acmicpc.net/problem/13301

import sys
n = int(sys.stdin.readline())
dp=[0]*(n+3)
dp[1]=4
dp[2]=6
for i in range(3,n+3):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])