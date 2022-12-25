# https://www.acmicpc.net/problem/11726

import sys
# nums = list(map(int, input().split()))
n = int(sys.stdin.readline())
dp = {}
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]
print(dp[n] % 10007)
