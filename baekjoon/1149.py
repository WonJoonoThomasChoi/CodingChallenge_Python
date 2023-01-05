# https://www.acmicpc.net/problem/1149

import sys
r = []
g = []
b = []
houses = int(sys.stdin.readline())
for _ in range(houses):
    price1, price2, price3 = map(int, sys.stdin.readline().split())
    r.append(price1)
    g.append(price2)
    b.append(price3)

dp= [ [0,0,0] for _ in range(houses)]
for i in range(houses):
    if i==0:
        dp[0]=([r[0], g[0], b[0]])
    else:
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + r[i]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + g[i]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + b[i]
print(min(dp[-1]))

