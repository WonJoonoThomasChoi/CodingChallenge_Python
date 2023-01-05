# https://www.acmicpc.net/problem/10826

import sys
a,b=0,1
for _ in range(int(sys.stdin.readline())):
    a,b=b,a+b
print(a)