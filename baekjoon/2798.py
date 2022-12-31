# https://www.acmicpc.net/problem/2798
import sys

n, target = list(map(int,sys.stdin.readline().split()))
cards = list(map(int,sys.stdin.readline().split()))

cmax = 0
for a in range(len(cards)-2):
    for b in range(a+1,len(cards)-1):
        for c in range(b+1,len(cards)):
            if cmax < cards[a]+cards[b]+cards[c] <= target:
                cmax = cards[a]+cards[b]+cards[c]
print(cmax)
