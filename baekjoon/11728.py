# https://www.acmicpc.net/problem/11728

import sys

a, b = map(int, sys.stdin.readline().split())
alist = list(map(int, sys.stdin.readline().split()))
blist = list(map(int, sys.stdin.readline().split()))
alist.sort()
blist.sort()
ans = []
ap = 0
bp = 0
while ap<a and bp<b:
    if alist[ap] > blist[bp]:
        ans.append(blist[bp])
        bp+=1
    else:
        ans.append(alist[ap])
        ap+=1
if ap == a:
    ans.extend(blist[bp:])
else:
    ans.extend(alist[ap:])
print(' '.join(map(str, ans)))
