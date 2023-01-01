# https://www.acmicpc.net/problem/4796

import sys
count=1
while True:
    l, p, v = list(map(int,sys.stdin.readline().split()))
    if l==p==v==0:
        break
    else:
        print("Case " + str(count) +": " +str((l*(v//p)) + min(v%p,l)))
        count+=1