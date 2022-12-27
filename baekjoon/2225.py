# https://www.acmicpc.net/problem/2225

import sys

nums = list(map(int, input().split()))
n = nums[0]
k = nums[1]

dp = {}
for i in range(n + 1):
    dp[(i, 1)] = 1

for l in range(n + 1):
    for j in range(1, k + 1):
        if (l, j) not in dp:
            temp = 0
            for i in range(l + 1):
                temp += dp[(i, j - 1)]
            dp[(l, j)] = temp
print(dp[n, k]%1000000000)
