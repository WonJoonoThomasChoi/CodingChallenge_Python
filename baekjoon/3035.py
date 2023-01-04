# https://www.acmicpc.net/problem/3035

import sys
R,C,ZR,ZC=map(int,sys.stdin.readline().split())
for i in range(R):
    s=sys.stdin.readline().rstrip()
    for j in range(ZR):
        for k in s:
            print(k*ZC,end="")
        print()