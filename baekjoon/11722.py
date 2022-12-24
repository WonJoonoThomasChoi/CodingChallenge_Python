#https://www.acmicpc.net/problem/11722
import sys

dp = [1 for x in range (int(sys.stdin.readline()))]
nums = list(map(int, input().split()))

for i in range(len(dp)):
    for j in range(i):
        if nums[i]<nums[j]:
            dp[i]=max(dp[i], dp[j]+1)
print(max(dp))
#10 30 10 20 20 10

