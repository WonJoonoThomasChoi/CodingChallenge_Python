# https://www.acmicpc.net/problem/4150

import sys
n=int(sys.stdin.readline())
a,b=0,1
for i in range(n):
    a,b=b,a+b
print(a)

