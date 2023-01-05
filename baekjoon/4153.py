# https://www.acmicpc.net/problem/4153

import sys
while True:
    alist = sorted(list(map(int, sys.stdin.readline().split())))
    if alist==[0,0,0]:
        break
    print('right' if alist[0]**2 + alist[1]**2 == alist[2]**2 else 'wrong')