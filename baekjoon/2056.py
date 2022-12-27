#https://www.acmicpc.net/problem/2056

ntasks = int(input())
dp={}

nums = list(map(int, input().split()))
dp[1] = nums[0]

for i in range(ntasks-1):
    nums = list(map(int, input().split()))
    time = nums[0]
    ntask = nums[1]
    pretask=[]
    if ntask!=0:
        time = time + max([ dp[x] for x in nums[2::]])
    dp[i+2] = time
print(max(dp.values()))

