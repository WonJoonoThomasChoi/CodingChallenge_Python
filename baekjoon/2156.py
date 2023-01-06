# https://www.acmicpc.net/problem/2156

import sys
n = int(sys.stdin.readline())
alist=[0]
dp=[0] * (n+1)
for _ in range(n):
    alist.append(int(sys.stdin.readline()))
if n==1:
    print(alist[1])
else:
    dp[1] = alist[1]
    dp[2] = alist[1] + alist[2]
    for i in range(3,n+1):
        dp[i] = max(dp[i-1], dp[i-2]+alist[i], dp[i-3]+alist[i-1]+alist[i])
    print(dp[-1])


'''
6
6
10
13
9
8
1
'''