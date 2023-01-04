# https://www.acmicpc.net/problem/2164

import sys
from collections import deque
n = int(sys.stdin.readline())
alist=deque(range(1,n+1))
for i in range(n-1):
    alist.popleft()
    alist.append(alist.popleft())
print(alist[0])