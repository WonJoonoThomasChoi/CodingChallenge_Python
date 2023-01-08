# https://www.acmicpc.net/problem/12852

import sys

n = int(sys.stdin.readline())

dp = [0] * (n + 1)
alist = []
dp[1] = dp[2] = dp[3] = 1

for i in range(4, n + 1):
    candid = dp[i - 1]
    num = i - 1
    if i % 3 == 0 and dp[i // 3] < candid:
        candid = dp[i // 3]
        num = i // 3
    if i % 2 == 0 and dp[i // 2] < candid:
        candid = dp[i // 2]
        num = i // 2
    dp[i] = candid + 1
    alist.append(num)

print(dp)
print(alist)
