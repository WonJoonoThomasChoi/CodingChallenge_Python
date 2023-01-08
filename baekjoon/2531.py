# https://www.acmicpc.net/problem/2531

import sys
n, d, k, c = map(int, sys.stdin.readline().split())
sushi = [int(sys.stdin.readline()) for _ in range(n)]
sushi.extend(sushi[:k-1])
cmax = 0
for i in range(n):
    tempset = set(sushi[i:k+i])
    tempset.add(c)
    cmax = max(cmax, len(tempset))
print(cmax)