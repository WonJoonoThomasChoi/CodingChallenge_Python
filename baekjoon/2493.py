# https://www.acmicpc.net/problem/2493

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ans = [0] * n
tlist = []
for i in range(1,n+1):
    # tlist[[4,4]]
    while tlist and tlist[-1][0] < nums[n-i]:
        ans[tlist[-1][1]] = n-i+1
        tlist.pop()
    tlist.append([nums[n-i], n-i])
print(*ans)

