# https://www.acmicpc.net/problem/17608

import sys
num, cmax, ans = int(sys.stdin.readline()), 0, 0
alist =[]
for _ in range(num):
    alist.append(int(sys.stdin.readline()))
for i in range(num-1,-1,-1):
    if alist[i] > cmax:
        cmax = alist[i]
        ans +=1
print(ans)