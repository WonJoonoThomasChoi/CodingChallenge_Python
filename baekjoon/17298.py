# https://www.acmicpc.net/problem/17298

import sys

input = sys.stdin.readline
astack = []
n = int(input())
alist = [[int(x), 0] for x in input().split()]
ans = [-1] * n
for i in range(len(alist)):
    alist[i][1] = i

for i in range(n):
    if len(astack) == 0 or astack[-1][0] >= alist[i][0]:
        astack.append(alist[i])
    else:
        while len(astack) != 0 and astack[-1][0] < alist[i][0]:
            ans[astack[-1][1]] = alist[i][0]
            astack.pop()
        astack.append(alist[i])
print(*ans)
