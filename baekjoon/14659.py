# https://www.acmicpc.net/problem/14659

import sys
n = int(sys.stdin.readline())
alist = list(map(int,sys.stdin.readline().split()))

ans=0
cmax = 0
count=0
for hill in alist:
    if hill>cmax:
        cmax = hill
        count=0
    else:
        count+=1
    ans = max(ans,count)
print(ans)


