# https://www.acmicpc.net/problem/9095
import sys

case = int(sys.stdin.readline())
dp = {}
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
for j in range(case):
    n = int(sys.stdin.readline())
    for i in range(4, n + 1):
        if i not in dp:
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    print(dp[n])

'''
1=1
2=11/2 2
3=2+1 111/12/21/3 4
4=1111/112/121/211/22/13/31 7
5=11111/2111/1211/1121/1112/221/212/122/311/131/113/32/23 13



'''
