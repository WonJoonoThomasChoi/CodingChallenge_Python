# https://www.acmicpc.net/problem/11052

import sys
n = int(sys.stdin.readline())
alist = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n + 1)
dp[1]=alist[0]
for j in range(2,n+1):
    temp=[alist[j-1]]
    for i in range(1, j):
        temp.append( dp[i]+dp[j-i] )
    dp[j]=max(temp)
print(dp[-1])

