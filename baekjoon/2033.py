# https://www.acmicpc.net/problem/2033

import math
import sys

n = sys.stdin.readline().rstrip()
alist = list(map(int, n))
lo=0
for i in range(len(n)-1,0,-1):
    if alist[i]+lo>=5:
        lo=1
    else:
        lo=0
    alist[i]=0
alist[0] +=lo
print(int("".join(map(str,alist))))
