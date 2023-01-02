# https://www.acmicpc.net/problem/2526

import sys
n,m=map(int, sys.stdin.readline().split())
alist = [n]

while True:
    temp = (alist[-1]*n)% m
    if temp not in alist:
        alist.append((alist[-1]*n)% m)
    else:
        print(len(alist)-alist.index(temp))
        break
