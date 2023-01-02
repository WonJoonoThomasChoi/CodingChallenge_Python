# https://www.acmicpc.net/problem/1834

import sys
n = int(sys.stdin.readline())
ans=0
for i in range(1,n):
    ans+=n*i + i
print(ans)
