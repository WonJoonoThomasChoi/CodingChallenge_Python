# https://www.acmicpc.net/problem/10219

import sys
cases = int(sys.stdin.readline())
for i in range(cases):
    n,m= map(int,sys.stdin.readline().split())
    alist=[]
    for i in range(n):
        alist.append(sys.stdin.readline().rstrip())
    for i in range(len(alist)):
        print(alist[i][::-1])