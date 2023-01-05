# https://www.acmicpc.net/problem/25644

import sys
input()
prices = list(map(int, sys.stdin.readline().split()))
max_profit = 0
min_price = sys.maxsize

for i in range(len(prices)):
    if prices[i]<min_price:
        min_price = prices[i]
    elif prices[i]-min_price > max_profit:
        max_profit = prices[i]-min_price
print(max_profit)


