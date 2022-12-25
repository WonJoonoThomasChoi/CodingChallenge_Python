import sys
n = int(sys.stdin.readline())
dp = [0 for x in range(n + 1)]
for i in range(2, n + 1):
    dp[i]=dp[i-1]+1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[int(i / 3)] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[int(i / 2)] + 1)
print(dp[-1])

'''
dp[1]=0
dp[2]=1
dp[3]=1
dp[4]=2
dp[5]=dp[4]+1 = 3
dp[6]=dp[2]+1 = 2
dp[7]=dp[6]+1 = 3
dp[8]=dp[4]+1 = 3
dp[9]=dp[3]+1 = 2
dp[10]=dp[9]+1 = 3
'''
