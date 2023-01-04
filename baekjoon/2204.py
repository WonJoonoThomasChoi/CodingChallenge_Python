# https://www.acmicpc.net/problem/2204

import sys
while True:
    n=int(sys.stdin.readline())
    if n==0:
        break
    alist=[]
    for i in range(n):
        alist.append((sys.stdin.readline().rstrip()))
    min = alist[0]
    for i in alist:
        if i.lower()<min.lower():
            min=i
    print(min)

