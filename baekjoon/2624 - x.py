#TODO: 반례찾아야함...
#https://www.acmicpc.net/problem/2624

target = int(input())
coins={}
numCoins = int(input())
for i in range(numCoins):
    coin = list(map(int, input().split()))
    coins[coin[0]] = coin[1]

dp = {}
dp[0] = 1
for i in range(numCoins):
    tempdplist = dp.copy()
    for j in tempdplist.keys():
        maxCoin = max(coins.keys())
        quantity = coins[maxCoin]
        for i in range(1,quantity+1):
            temp=maxCoin*i+j
            if temp>target:
                break
            if temp not in dp:
                dp[temp] = 1
            else:
                dp[temp] += tempdplist[j]
    del coins[maxCoin]
if target not in dp:
    print(0)
else:
    print(dp[target])



'''
d a c b b c d

'''